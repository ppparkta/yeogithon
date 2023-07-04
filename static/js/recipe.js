window.onload = () => {
    const likeButtons = document.querySelectorAll('.fa-regular.fa-heart');
    const menus = document.querySelectorAll('#menu1');

    likeButtons.forEach((like) => {
        const ggimButton = like.parentElement;

        ggimButton.style.background = 'none';
        like.classList.remove("fa-solid");

        ggimButton.addEventListener("click", (e) => {
            like.classList.toggle("fa-solid");
        });
    });

    menus.forEach((menu) => {
        const randomColor = getRandomColor();
        menu.style.backgroundColor = randomColor;
    });

    function getRandomColor() {
        const colors = ["#FFEDD2", "#E1D9FF", "#D9EDFF"];
        const randomIndex = Math.floor(Math.random() * colors.length);
        return colors[randomIndex];
    }
}