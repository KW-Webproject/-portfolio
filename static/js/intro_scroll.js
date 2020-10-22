const menu = document.querySelector(".nav__menu");
let selected = document.querySelector(".selected");


const home__height1 = document.querySelector("#home").getBoundingClientRect().height;
const home__height2 = document.querySelector("#responsive").getBoundingClientRect().height;
const skill_top = document.querySelector("#skills").getBoundingClientRect().top;
const skill_height = document.querySelector("#skills").getBoundingClientRect().height;
const team_top = document.querySelector("#team").getBoundingClientRect().top;
const team_height = document.querySelector("#team").getBoundingClientRect().height;

const home = home__height1 + home__height2;
const skill = home + skill_height;
const team = skill + team_height;

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
    } else if (home < window.scrollY && window.scrollY < skill) {
        selected.classList.remove("selected");
        document.querySelector(".skills").classList.add("selected");
        selected = document.querySelector(".skills")
    } else if (skill < window.scrollY && window.scrollY < team) {
        selected.classList.remove("selected");
        document.querySelector(".team").classList.add("selected");
        selected = document.querySelector(".team")
    }
})