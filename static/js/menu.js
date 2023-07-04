
function count1(type)  {
    const resultElement = document.getElementById('result1');
    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;

    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;

  }

  function count2(type)  {

    const resultElement = document.getElementById('result2');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;

    }else if(type === 'minus')  {
      number = parseInt(number) - 1;

    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;
  }

  function count3(type)  {
    const resultElement = document.getElementById('result3');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;
  }
  function count4(type)  {
    const resultElement = document.getElementById('result4');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;

  }

  function count5(type)  {
    const resultElement = document.getElementById('result5');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;
  }
  function count6(type)  {
    const resultElement = document.getElementById('result6');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;
}
function count7(type)  {
    const resultElement = document.getElementById('result7');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;
  }

  function count8(type)  {
    const resultElement = document.getElementById('result8');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;
  }
  function count9(type)  {
    const resultElement = document.getElementById('result9');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;
  }
  function count10(type)  {
    const resultElement = document.getElementById('result10');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;
  }
  function count11(type)  {
    const resultElement = document.getElementById('result11');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;
  }
  function count12(type)  {
    const resultElement = document.getElementById('result12');

    let number = resultElement.innerText;

    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    if(parseInt(number)<0){
        number=0
    }
    resultElement.innerHTML= number;}

// 색상 변경 및 버튼 클릭 시 보이도록
const numbutton=document.querySelector("#numbutton")
  const btnbeige1=document.getElementById("menu1");
  const btnbeige2=document.getElementById("menu5");
  const btnbeige3=document.getElementById("menu9");

  btnbeige1.addEventListener("click",(e)=>{
   menu1.style.backgroundColor="#FFF6EA";
   btnvisible1();

  })
  btnbeige2.addEventListener("click",(e)=>{
    menu5.style.backgroundColor="#FFF6EA";
    btnvisible5();
   })
   btnbeige3.addEventListener("click",(e)=>{
    menu9.style.backgroundColor="#FFF6EA";
    btnvisible9();
   })

   const btnpink1=document.getElementById("menu2");
   const btnpink2=document.getElementById("menu6");
   const btnpink3=document.getElementById("menu10");

   btnpink1.addEventListener("click",(e)=>{
    menu2.style.backgroundColor="#f8e3e3";
    btnvisible2();
   })
   btnpink2.addEventListener("click",(e)=>{
    menu6.style.backgroundColor="#f8e3e3";
    btnvisible6();
   })

   btnpink3.addEventListener("click",(e)=>{
    menu10.style.backgroundColor="#f8e3e3";
    btnvisible10();
   })

   const btnblue1=document.getElementById("menu3");
   const btnblue2=document.getElementById("menu7");
   const btnblue3=document.getElementById("menu11");

   btnblue1.addEventListener("click",(e)=>{
    menu3.style.backgroundColor="#E7F3FF";
    btnvisible3();

   })
   btnblue2.addEventListener("click",(e)=>{
    menu7.style.backgroundColor="#E7F3FF";
    btnvisible7();
   })

   btnblue3.addEventListener("click",(e)=>{
    menu11.style.backgroundColor="#E7F3FF";
    btnvisible11();
   })

   const btnyellow1=document.getElementById("menu4");
   const btnyellow2=document.getElementById("menu8");
   const btnyellow3=document.getElementById("menu12");

   btnyellow1.addEventListener("click",(e)=>{
    menu4.style.backgroundColor="#f6e2d0";
    btnvisible4();
   })
   btnyellow2.addEventListener("click",(e)=>{
    menu8.style.backgroundColor="#f6e2d0";
    btnvisible8();
   })

   btnyellow3.addEventListener("click",(e)=>{
    menu12.style.backgroundColor="#f6e2d0";
    btnvisible12();
   })

   function btnvisible1(){
    numbutton1.setAttribute('class','active')

}function btnvisible2(){
    numbutton2.setAttribute('class','active')

}function btnvisible3(){
    numbutton3.setAttribute('class','active')

}function btnvisible4(){
    numbutton4.setAttribute('class','active')

}function btnvisible5(){
    numbutton5.setAttribute('class','active')

}function btnvisible6(){
    numbutton6.setAttribute('class','active')

}function btnvisible7(){
    numbutton7.setAttribute('class','active')

}function btnvisible8(){
    numbutton8.setAttribute('class','active')

}function btnvisible9(){
    numbutton9.setAttribute('class','active')

}function btnvisible10(){
    numbutton10.setAttribute('class','active')

}function btnvisible11(){
    numbutton11.setAttribute('class','active')

}function btnvisible12(){
    numbutton12.setAttribute('class','active')

}

function cancle(){
    btnyellow1.removeEventListener("click",(e)=>{
        menu4.style.backgroundColor="#f6e2d0";
        btnvisible4();
       })

}
