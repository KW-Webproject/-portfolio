window.addEventListener('load', () => {
    const reBtn = document.querySelector("#re-btn");
    const content = document.querySelector(".contents");
    const sections = document.querySelectorAll("section");

    reBtn.addEventListener("click", () => {
        setSpinValue(0);
    });

    reBtn2.addEventListener("click", () => {
        setSpinValue(0);
    });

    function scrollContent(count) {
        console.log(count);
        content.setAttribute('style', `transform: translateX(-${count * 100}vw);`);
    }
    function setSpinValue(spin_value) {
        console.log(spin_value);
        if (spin_value == 0) {
            //첫번째 폼일때
            spin_value = 1;
        } else {
            spin_value = 0;
        }
        scrollContent(spin_value);
    }


});