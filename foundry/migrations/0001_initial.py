# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Link'
        db.create_table('foundry_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('view_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['category.Category'], null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('foundry', ['Link'])

        # Adding model 'Menu'
        db.create_table('foundry_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=32, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('display_title', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('foundry', ['Menu'])

        # Adding model 'Navbar'
        db.create_table('foundry_navbar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=32, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('foundry', ['Navbar'])

        # Adding model 'Listing'
        db.create_table('foundry_listing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=32, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['category.Category'], null=True, blank=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('display_primary_category', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('display_likes', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('foundry', ['Listing'])

        # Adding M2M table for field content on 'Listing'
        db.create_table('foundry_listing_content', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('listing', models.ForeignKey(orm['foundry.listing'], null=False)),
            ('modelbase', models.ForeignKey(orm['jmbo.modelbase'], null=False))
        ))
        db.create_unique('foundry_listing_content', ['listing_id', 'modelbase_id'])

        # Adding model 'MenuLinkPosition'
        db.create_table('foundry_menulinkposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foundry.Link'])),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('condition_expression', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foundry.Menu'])),
        ))
        db.send_create_signal('foundry', ['MenuLinkPosition'])

        # Adding model 'NavbarLinkPosition'
        db.create_table('foundry_navbarlinkposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foundry.Link'])),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('condition_expression', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('navbar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foundry.Navbar'])),
        ))
        db.send_create_signal('foundry', ['NavbarLinkPosition'])

        # Adding model 'Member'
        db.create_table('foundry_member', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('crop_from', self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='member_related', null=True, to=orm['photologue.PhotoEffect'])),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('twitter_username', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal('foundry', ['Member'])

        # Adding model 'DefaultAvatar'
        db.create_table('foundry_defaultavatar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('crop_from', self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='defaultavatar_related', null=True, to=orm['photologue.PhotoEffect'])),
        ))
        db.send_create_signal('foundry', ['DefaultAvatar'])

        # Adding model 'Country'
        db.create_table('foundry_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=32, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('minimum_age', self.gf('django.db.models.fields.PositiveIntegerField')(default=18)),
        ))
        db.send_create_signal('foundry', ['Country'])

        # Adding model 'Page'
        db.create_table('foundry_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=32, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('is_homepage', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('foundry', ['Page'])

        # Adding M2M table for field sites on 'Page'
        db.create_table('foundry_page_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['foundry.page'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('foundry_page_sites', ['page_id', 'site_id'])

        # Adding model 'Row'
        db.create_table('foundry_row', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foundry.Page'])),
            ('index', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('block_name', self.gf('django.db.models.fields.CharField')(default='content', max_length=32)),
        ))
        db.send_create_signal('foundry', ['Row'])

        # Adding model 'Column'
        db.create_table('foundry_column', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foundry.Row'])),
            ('index', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=8)),
        ))
        db.send_create_signal('foundry', ['Column'])

        # Adding model 'Tile'
        db.create_table('foundry_tile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('column', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foundry.Column'])),
            ('index', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('target_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tile_target_content_type', null=True, to=orm['contenttypes.ContentType'])),
            ('target_object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('view_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('class_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('enable_ajax', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('condition_expression', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('foundry', ['Tile'])

        # Adding model 'FoundryComment'
        db.create_table('foundry_foundrycomment', (
            ('comment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['comments.Comment'], unique=True, primary_key=True)),
            ('in_reply_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foundry.FoundryComment'], null=True, blank=True)),
        ))
        db.send_create_signal('foundry', ['FoundryComment'])


    def backwards(self, orm):
        
        # Deleting model 'Link'
        db.delete_table('foundry_link')

        # Deleting model 'Menu'
        db.delete_table('foundry_menu')

        # Deleting model 'Navbar'
        db.delete_table('foundry_navbar')

        # Deleting model 'Listing'
        db.delete_table('foundry_listing')

        # Removing M2M table for field content on 'Listing'
        db.delete_table('foundry_listing_content')

        # Deleting model 'MenuLinkPosition'
        db.delete_table('foundry_menulinkposition')

        # Deleting model 'NavbarLinkPosition'
        db.delete_table('foundry_navbarlinkposition')

        # Deleting model 'Member'
        db.delete_table('foundry_member')

        # Deleting model 'DefaultAvatar'
        db.delete_table('foundry_defaultavatar')

        # Deleting model 'Country'
        db.delete_table('foundry_country')

        # Deleting model 'Page'
        db.delete_table('foundry_page')

        # Removing M2M table for field sites on 'Page'
        db.delete_table('foundry_page_sites')

        # Deleting model 'Row'
        db.delete_table('foundry_row')

        # Deleting model 'Column'
        db.delete_table('foundry_column')

        # Deleting model 'Tile'
        db.delete_table('foundry_tile')

        # Deleting model 'FoundryComment'
        db.delete_table('foundry_foundrycomment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'category.category': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['category.Category']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'category.tag': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Tag'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['category.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'comments.comment': {
            'Meta': {'ordering': "('submit_date',)", 'object_name': 'Comment', 'db_table': "'django_comments'"},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_type_set_for_comment'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_pk': ('django.db.models.fields.TextField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'submit_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comment_comments'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'foundry.column': {
            'Meta': {'object_name': 'Column'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foundry.Row']"}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '8'})
        },
        'foundry.country': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_age': ('django.db.models.fields.PositiveIntegerField', [], {'default': '18'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'foundry.defaultavatar': {
            'Meta': {'object_name': 'DefaultAvatar'},
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'defaultavatar_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'foundry.foundrycomment': {
            'Meta': {'ordering': "('submit_date',)", 'object_name': 'FoundryComment', '_ormbases': ['comments.Comment']},
            'comment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['comments.Comment']", 'unique': 'True', 'primary_key': 'True'}),
            'in_reply_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foundry.FoundryComment']", 'null': 'True', 'blank': 'True'})
        },
        'foundry.link': {
            'Meta': {'object_name': 'Link'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['category.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'view_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'foundry.listing': {
            'Meta': {'object_name': 'Listing'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['category.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jmbo.ModelBase']", 'null': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'display_likes': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'display_primary_category': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'foundry.member': {
            'Meta': {'object_name': 'Member', '_ormbases': ['auth.User']},
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'member_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'foundry.menu': {
            'Meta': {'object_name': 'Menu'},
            'display_title': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'foundry.menulinkposition': {
            'Meta': {'ordering': "('position',)", 'object_name': 'MenuLinkPosition'},
            'condition_expression': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foundry.Link']"}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foundry.Menu']"}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'foundry.navbar': {
            'Meta': {'object_name': 'Navbar'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'foundry.navbarlinkposition': {
            'Meta': {'ordering': "('position',)", 'object_name': 'NavbarLinkPosition'},
            'condition_expression': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foundry.Link']"}),
            'navbar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foundry.Navbar']"}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'foundry.page': {
            'Meta': {'object_name': 'Page'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'foundry.row': {
            'Meta': {'object_name': 'Row'},
            'block_name': ('django.db.models.fields.CharField', [], {'default': "'content'", 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foundry.Page']"})
        },
        'foundry.tile': {
            'Meta': {'object_name': 'Tile'},
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'column': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['foundry.Column']"}),
            'condition_expression': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'enable_ajax': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'target_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tile_target_content_type'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'target_object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'view_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'jmbo.modelbase': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'ModelBase'},
            'anonymous_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'anonymous_likes': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['category.Category']", 'null': 'True', 'blank': 'True'}),
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'comments_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comments_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'modelbase_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'likes_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'likes_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'primary_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'primary_modelbase_set'", 'null': 'True', 'to': "orm['category.Category']"}),
            'publish_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'publishers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['publisher.Publisher']", 'null': 'True', 'blank': 'True'}),
            'retract_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'unpublished'", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['category.Tag']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.59999999999999998'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'publisher.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'secretballot.vote': {
            'Meta': {'unique_together': "(('token', 'content_type', 'object_id'),)", 'object_name': 'Vote'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vote': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['foundry']
