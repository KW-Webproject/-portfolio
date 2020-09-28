window.addEventListener('load', ()=>{
    const sections = document.querySelectorAll('section');
    const content = document.querySelector('.main_contents');
    const arrowUp = document.querySelector('.arrowUp');
    if(window.innerWidth > 1024){
        let spin_value = 0;
        let can_scroll = true;

        window.addEventListener('mousewheel', (e) => {
            if(can_scroll){
                can_scroll = false;
                if(e.deltaY > 0){   
                    //scroll down
                    if(spin_value < sections.length - 1) {
                        spin_value += 1;
                        drawArrow();}
                }else{
                    //scroll up
                    if(spin_value > 0) {
                        spin_value -=1;
                    }
                        if(spin_value == 0)removeArrow();
                        
                }
                setTimeout(() => {can_scroll = true}, 560);
            }
            scrollContents(spin_value);
        });

        window.addEventListener('keydown', (e) => {
            if(can_scroll){
                can_scroll = false;
                if(e.keyCode == 40){   
                    //KEY down
                    if(spin_value < sections.length - 1) spin_value += 1;
                }else if(e.keyCode == 38){
                    //KEY up
                    if(spin_value > 0) spin_value -=1;
                    if(spin_value == 0)removeArrow();
                }
                setTimeout(() => {can_scroll = true}, 560);
            }

            scrollContents(spin_value);
        });

        arrowUp.addEventListener('click', ()=>{
            content.setAttribute('style', `transform: translateY(0);`);
            removeArrow();
            spin_value = 0;
        }); 
        }

        function drawArrow(){
            arrowUp.classList.add('visible');
        }
        function removeArrow(){
            arrowUp.classList.remove('visible');
        }
        function scrollContents(count){
            content.setAttribute('style', `transform: translateY(-${count*100}vh);`);
        }

});
