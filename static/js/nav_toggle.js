const navToggle = document.querySelector(".nav_toggle");
const nav = document.querySelector(".header__nav");
navToggle.addEventListener("click", () => {
    nav.classList.toggle("open");
});