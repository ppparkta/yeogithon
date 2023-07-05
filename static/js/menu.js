var total = 0;
var totalElement = document.getElementById("total");

function handleMenuClick(menu) {
  var numButton = menu.querySelector("#numbutton");


  if (numButton.style.display === "" || numButton.style.display === "none") {
    numButton.style.display = "flex";

    menu.style.backgroundColor="#FFF6EA"
  }


  var totalElement = document.getElementById("total");
  var total = 0;
  var numButtons = document.querySelectorAll("#numbutton");
  for (var i = 0; i < numButtons.length; i++) {
    var count = parseInt(numButtons[i].dataset.count);
    total += count;
  }
  totalElement.textContent = total;
}

function countA(button) {
  var numButton = button.parentElement;
  var countElement = numButton.querySelector("#result");
  var currentCount = parseInt(numButton.dataset.count);

  if (currentCount > 1) {
    numButton.dataset.count = currentCount - 1;
    countElement.textContent = numButton.dataset.count;
    total--;
    totalElement.textContent = total;
  }
}

function countB(button) {
  var numButton = button.parentElement;
  var countElement = numButton.querySelector("#result");
  var currentCount = parseInt(numButton.dataset.count);

  numButton.dataset.count = currentCount + 1;
  countElement.textContent = numButton.dataset.count;
  total++;
  totalElement.textContent = total;
}


function resetCounts() {
  var numButtons = document.querySelectorAll("#numbutton");
  var menus = document.querySelectorAll("#menu");

  for (var i = 0; i < numButtons.length; i++) {
    var numButton = numButtons[i];
    numButton.dataset.count = 1;
    numButton.querySelector("#result").textContent = 1;
    numButton.classList.remove("active");
    numButton.style.display = "none";
  }

  for (var i = 0; i < menus.length; i++) {
    var menu = menus[i];
    var numButton = menu.querySelector("#numbutton");
    numButton.classList.remove("active");
    menu.style.backgroundColor = "white";
  }

  var totalElement = document.getElementById("total");
  totalElement.textContent = 0;
}