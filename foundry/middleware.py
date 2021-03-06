import re

from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user

from django.http import HttpResponseRedirect

from preferences import preferences


PROTECTED_URLS_PATTERN = r'|'.join((
    reverse('age-gateway'), 
    reverse('join'), 
    reverse('login'), 
    '/password_reset', 
    '/static', 
    '/admin'
))


class VerboseRequestMeta:
    """Add metadata to request so repr(request) prints more information. Runs
    as one of the last middleware."""

    def process_request(self, request):
        user = getattr(request, 'user', None)
        if user is not None:
            request.META['AUTHENTICATED_USER'] = str(user)


class AgeGateway:
    """Combined private site and age gateway. Due to legacy this name is used.
    Must run after AuthenticationMiddleware."""

    def process_response(self, request, response):
        
        # Ignore ajax
        if request.is_ajax():
            return response
        
        # Protected URLs
        if re.match(PROTECTED_URLS_PATTERN, request.META['PATH_INFO']) is not None:
            return response

        # Now only do we hit the database
        # xxx: investigate preference caching. May want to hit the db less.
        private_site = preferences.GeneralPreferences.private_site
        show_age_gateway = preferences.GeneralPreferences.show_age_gateway

        # Check trivial case
        if not (private_site or show_age_gateway):
            return response

        # Private site not enabled and gateway passed
        if not private_site and request.COOKIES.get('age_gateway_passed'):
            return response

        # Exempted URLs
        exempted_urls = preferences.GeneralPreferences.exempted_urls        
        if exempted_urls \
            and (
                re.match(
                    r'|'.join(exempted_urls.split()), 
                    request.META['PATH_INFO']
               ) is not None
            ):
            return response

        user = getattr(request, 'user', None)
        if (user is not None) and user.is_anonymous():
            if private_site:
                return HttpResponseRedirect(reverse('login'))
            else:
                return HttpResponseRedirect(reverse('age-gateway'))

        return response            


class PaginationMiddleware:
    """Our replacement for django-pagination PaginationMiddleware. It defaults
    to the last page if no page is set on the request. A monkey patch in
    monkey.py handles the negative page number."""

    def process_request(self, request):       
        page = -1
        try:
            page = int(request.REQUEST['page'])
        except (KeyError, ValueError, TypeError):
            pass
        request.__class__.page = page
        
class MembersOnlineStatusMiddleware(object):
    """Cache MembersOnlineStatus instance for an authenticated member"""
    
    def process_request(self, request):
        
        MEMBERS_ONLINE_CACHE_TAG = 'MEMBERS_ONLINE'
        
        user = get_user(request)
        
        if not user.is_authenticated() or not hasattr(user,'member'):
            return
        
        MEMBER_ONLINE_CACHE_TAG = 'USER_%d_MEMBER_ONLINE' % user.id
        
        cache.set(MEMBER_ONLINE_CACHE_TAG, 
                  MEMBER_ONLINE_CACHE_TAG, 
                  settings.MEMBERS_ONLINE_TIMEOUT)
        
        online_members = cache.get(MEMBERS_ONLINE_CACHE_TAG)
        
        if not online_members:
            online_members = []
            
        if user.id not in online_members:
            online_members.append(user.id)
        
        for member_id in online_members:
            if not cache.get('USER_%d_MEMBER_ONLINE' % member_id):
                online_members.remove(member_id)
                
        cache.set(MEMBERS_ONLINE_CACHE_TAG, 
                  online_members, 
                  settings.MEMBERS_ONLINE_TIMEOUT * 5)
        
        return
