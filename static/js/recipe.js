//작성하기 버튼 누르면 박스 생성되고 글 작성하는 기능 구현해야함
//작성자 본인의 글에는 수정, 삭제 버튼 필요

window.onload = () => {
    const likeButtons = document.querySelectorAll('.fa-regular.fa-heart');

    likeButtons.forEach((like) => {
        const ggimButton = like.parentElement;

        ggimButton.style.background = 'none';
        like.classList.remove("fa-solid");

        ggimButton.addEventListener("click", (e) => {
            like.classList.toggle("fa-solid");
        });
    });
}