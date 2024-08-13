$(document).ready(function() {
    $('.blog-flex-content-item-reactions-item-image-water').click(function(event) {
        
        var post_pk = $(this).data('pk');
        var url = '/blog/put_water/' + post_pk + '/';

        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value,
            },

            success: function(response) {
                $('.blog-flex-content-item-reactions-item-amount-water').each(function() {
                    var item = $(this);
                    if (item.data('pk') == post_pk) {
                        item.text(response.count_water);
                    }
                });
            },
        });
    });
});