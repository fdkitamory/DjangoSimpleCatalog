/**
 * Created by frank on 12.02.15.
 */

document.addEventListener( "DOMContentLoaded", function(){

    function get_search_results(){

        $.ajax({
            url: '/search_ajax/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                q: $('#search_text').val()
            },
            dataType: 'html',
            success: function(response) {
                $('.prod_list__item').remove();
                $('.pagination').remove();
                $('.prod_list').append(response);
            }
        })
    }

    $('#search_button').click(function (){
        get_search_results();
    });

})
