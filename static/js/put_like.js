$(document).ready(function() {
    $('.blog-flex-content-item-reactions-item-image').click(function(event) {
        
        var post_pk = $(this).data('pk');
        var url = '/blog/put_like/' + post_pk;

        $.ajax({
            url: url,
            type: 'GET',

            success: function(response) {
                $('.blog-flex-content-item-reactions-item-amount').each(function() {
                    var item = $(this);
                    if (item.data('pk') == post_pk) {
                        item.css('color', response.color_text);
                        item.text(response.count_likes);
                    }
                });
            },
        });
    });
});