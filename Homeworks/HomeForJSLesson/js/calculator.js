var x = "";
var input = $("#display");
$(".btn-dark").click(function() {
   x += $(this).text();
   input.val(x);
   console.log(x)});
$(".btn-primary").click(function() {
    x = eval(input.val());
    input.val(x);});
$(".btn-light").click(function(){
   x = "";
   input.val("0");});