const color = document.querySelector(".colors__bottom");
const button = document.querySelectorAll(".full__top i");
const fullpages = document.querySelectorAll(".colors__full");
let flag = false; // 4컷 false!

color.addEventListener("click", (e) => {
    const target = e.target;
    if (target.classList.contains("fas")) {
        addHide(target);
        return;
    }
    color.classList.add("dontclick");
    target.classList.remove("hide");
});


function addHide(target) {
    console.log(target);
    fullpages.forEach((page) => {
        if (!page.classList.contains("hide")) {
            page.classList.add("hide");
            color.classList.remove("dontclick");

        }
    })
}

// 1. color__bottom을 클릭하면 => 먼저 color__bottom 클릭이 안되게 하고, target의 hide를 제거한다.
//2. color__bottom을 클릭해서 full page가 떠있는 상태면, i만 클릭이 된다. target이 i일 경우,
//   i에 해당하는 함수를 실행시킨다(해당 이벤트는 종료) => 그리고 page 중에 hide가 없는 page를 발견할 경우,
//   hide를 더해서 다시 fullpage를 안보이게 만들고 color__bottom의 dontclick 클래스를 제거한다.(클릭 가능)

//scroll안되게!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!