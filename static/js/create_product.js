// 이미지 업로드 시 이미지 미리보기
const fileUpload = document.getElementById("chooseFile");
const box = document.querySelector(".box");
const imageShow = document.getElementById("image-show");

fileUpload.addEventListener("change", (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = (e) => {
    const img = document.createElement("img");
    img.src = e.target.result;
    img.classList.add("img");
    imageShow.innerHTML = "";
    imageShow.appendChild(img);
  };

  reader.readAsDataURL(file);
});