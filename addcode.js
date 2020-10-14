$(document).ready(function(){

    $.ajax({url: "hello.php", success: function(result){
        $("#ajaxElement").html(result);    
    }});

});
