$(function () {
    $('.js-send').click(function(){
        var url = $(this).attr('data-url');
        var message = $(".js-user_data").val();
        $.ajax({
            type: 'get',
            url: url,
            dataType: 'json',
            data: {'message':message},
            async: true,
            success: function (data){
                $('#js-div_for_text').text(data.message)
            },
            error: function(){
                console.error('500 - server error');
            }
        });
    });

    $('.js-send2').click(function(){
        var url = $(this).data('url');
        var message = $(".js-user_data").val();
        $.ajax({
            type: 'get',
            url: url,
            dataType: 'html',
            data: {'message':message},
            async: true,
            success: function (data){
                console.log(data.message);
                $('#js-div_for_text').text(data.message)
            },
            error: function(){
                console.error('500 - server error');
            }
        });
    });

    $('.form').submit(function(e){
        e.preventDefault();
        var data = $(this).serialize();
        $.ajax({
            type: 'post',
            // url: url,
            dataType: 'json',
            data: data,
            async: true,
            success: function (data){
                $('#js-div_for_text').text(data.message)
            },
            error: function(){
                console.error('500 - server error');
            }
        });
    });
});
