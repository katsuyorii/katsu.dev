$(document).ready(function() {
    $('.blog-flex-content-item-reactions-item-image-like').click(function(event) {
        
        var post_pk = $(this).data('pk');
        var url = '/blog/put_like/' + post_pk + '/';

        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value,
            },

            success: function(response) {
                $('.blog-flex-content-item-reactions-item-amount-like').each(function() {
                    var item = $(this);
                    if (item.data('pk') == post_pk) {
                        item.text(response.count_likes);
                    }
                });
            },
        });
    });
});