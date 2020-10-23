const menu = document.querySelector(".nav__menu");
let selected = document.querySelector(".selected");


const home = document.querySelector("#home").getBoundingClientRect().height;
const serviceHeight = document.querySelector("#service").getBoundingClientRect().height;
const skillHeight = document.querySelector("#skills").getBoundingClientRect().height;
const teamHeight = document.querySelector("#team").getBoundingClientRect().height;

const service = home + serviceHeight;
const skill = service + skillHeight;
const team = skill + teamHeight;

const toggle = document.querySelector(".header__toggle");
const nav = document.querySelector(".header__nav");


toggle.addEventListener("click", (e) => {
    console.log(e);
    toggle.classList.toggle("open");
    nav.classList.toggle("open");
})
menu.addEventListener("click", (event) => {
    const target = event.target;
    const link = target.dataset.link;
    const scrollTo = document.querySelector(link);
    scrollTo.scrollIntoView({ behavior: "smooth" });

    selected.classList.remove("selected");
    target.classList.add("selected");
    selected = target;
});

window.addEventListener("scroll", () => {
    if (0 < window.scrollY && window.scrollY < home) {
        selected.classList.remove("selected");
        document.querySelector(".about").classList.add("selected");
        selected = document.querySelector(".about")
    } else if (home < window.scrollY && window.scrollY < service) {
        selected.classList.remove("selected");
        document.querySelector(".service").classList.add("selected");
        selected = document.querySelector(".service")
    } else if (service < window.scrollY && window.scrollY < skill) {
        selected.classList.remove("selected");
        document.querySelector(".skills").classList.add("selected");
        selected = document.querySelector(".skills")
    } else if (skill < window.scrollY && window.scrollY < team) {
        selected.classList.remove("selected");
        document.querySelector(".team").classList.add("selected");
        selected = document.querySelector(".team")
    }
})