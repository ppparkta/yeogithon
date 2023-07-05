const menu = document.getElementById('menu');
const colors = ['#FFF6EA', '#f8e3e3', ' #E7F3FF', '#f6e2d0'];
const randomColor = getRandomColor(colors);
menu.style.setProperty('--random-color', randomColor);

function getRandomColor(colorArray) {
  return colorArray[Math.floor(Math.random() * colorArray.length)];
}