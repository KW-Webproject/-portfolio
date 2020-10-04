
const masks = document.querySelectorAll('.main_container .txt--mask');

window.addEventListener('load', ()=>{
    masks.forEach((mask)=>{  
        setTimeout((mask) => mask.classList.add('active'), 200);
    });
});