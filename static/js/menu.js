var total = 0;
var totalElement = document.getElementById("total");


function handleMenuClick(menu) {
  var numButton = menu.querySelector("#numbutton");

  if (numButton.style.display === "" || numButton.style.display === "none") {
    numButton.style.display = "flex";
    menu.style.backgroundColor = "#FFF6EA";
    total++;
    totalElement.textContent = total;
  }
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

  total = 0;
  totalElement.textContent = total;
}

function redirectToCartPage() {
  window.location.href = "http://127.0.0.1:8000/cart/";
}