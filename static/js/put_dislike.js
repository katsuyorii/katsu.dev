$(document).ready(function() {
    $('.blog-flex-content-item-reactions-item-image-dis').click(function(event) {
        
        var post_pk = $(this).data('pk');
        var url = '/blog/put_dislike/' + post_pk;

        $.ajax({
            url: url,
            type: 'GET',

            success: function(response) {
                $('.blog-flex-content-item-reactions-item-amount-dis').each(function() {
                    var item = $(this);
                    if (item.data('pk') == post_pk) {
                        item.text(response.count_dislikes);
                    }
                });
            },
        });
    });
});