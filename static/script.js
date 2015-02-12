/**
 * Created by frank on 12.02.15.
 */

document.addEventListener( "DOMContentLoaded", function(){

    function get_search_results(){

        $.ajax({
            url: '/search_ajax',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').value,
                q: $('#search_text').val()
            },
            dataType: 'html',
            context: $this,
            success: function(response) {

            },
            error: function(xhr, error, status) {
                alert(error);
                $this.find('img.loading').remove();
                $this.find('.dt').show();
            }
        })
    }

    $('#search_button').click(function (){
        get_search_results();
    });

})
