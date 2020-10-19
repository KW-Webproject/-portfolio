const navToggle = document.querySelector(".nav__toggle");
const nav = document.querySelector(".header__nav");
navToggle.addEventListener("click", () => {
    console.log("hi");
    nav.classList.toggle("open");
});