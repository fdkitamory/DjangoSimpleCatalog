/**
 * Created by frank on 12.02.15.
 */

document.addEventListener( "DOMContentLoaded", function(){

    function get_search_results(){
        $.post(
            "/search_ajax/",
            {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').value,
                'q': $('#search_text').val()
            },
            onAjaxSuccess
        );

        function onAjaxSuccess(data) {
          // Здесь мы получаем данные, отправленные сервером и выводим их на экран.
          console.log(data)
        }

        console.log()
        console.log()
    }

    $('#search_button').click(function (){
        get_search_results();
    });

})