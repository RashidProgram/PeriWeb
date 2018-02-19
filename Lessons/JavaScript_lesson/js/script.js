console.log(document.getElementById("fish").innerHTML);
document.getElementById("fish").innerHTML = "Мага беги пока султанмурад не пришел";
console.log(document.getElementsByTagName("div")[0].innerHTML);
console.log(document.getElementsByClassName("loremBig")[0].innerHTML);

console.log(document.querySelector("div .q").innerHTML);
console.log(document.querySelector("div .q").setAttribute("title","dfsa"));


document.getElementById("fish").onclick = function(){
    console.log("пЛОТи нАЛОГи");
};
function q(obj){
    obj.setAttribute("style","background-color:wheat;height:100px;")
};