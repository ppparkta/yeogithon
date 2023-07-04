var sum = function(){
    var price1 = parseFloat(document.getElementById("price1").innerText);
    var price2 = parseFloat(document.getElementById("price2").innerText);
    var result1 = parseInt(document.getElementById("result1").innerText);
    var result2 = parseInt(document.getElementById("result2").innerText);

    totalprice = (price1 * 1000 * result1) + (price2 * 1000 * result2);
    document.getElementById("total").innerText = totalprice + "원";
}

var count1=1;
var count1A=function(){
  count1 = count1 - 1;
  if(count1<1){count1=1}
  document.getElementById("result1").innerText=count1;
  sum();
}

function count1B(){
  count1 = count1 + 1;
  document.getElementById("result1").innerText=count1;
  sum();
}

var count2=1;
var count2A=function(){
  count2 = count2-1;
  if(count2<1){count2=1}
  document.getElementById("result2").innerText=count2;
  sum();
}

var count2B=function(){
  count2 = count2+1;
  document.getElementById("result2").innerText=count2;
  sum();
}

window.onload = function() {
    sum();
};