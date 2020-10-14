function doRefresh() {
    $("#ajaxElement").load('hello.php');
}
$(function() {
    setInterval(doRefresh, 1000);
});
