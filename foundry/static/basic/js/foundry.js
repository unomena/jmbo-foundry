$(document).ready(function(){

    $('div.paged_results a').live('click', function(e){
        e.preventDefault();
        var target = $(this).parents('div.foundry-enable-ajax:first');
        var url = target.attr('original_url');
        url = url + $(this).attr('href');
        $.get(
            url, 
            {}, 
            function(data){
                if (data.search('id="content"') != -1)
                {
                    // Markup that contains fluff. We want only the content.
                    var el = $('<div>' + data + '</div>');                   
                    var content = $('div#content', el);
                    target.html(content.html());
                }
                else
                    target.html(data);
            }
        );
    });

});