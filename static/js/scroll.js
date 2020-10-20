//Main-Down-Button

const downBtn = document.querySelector(".down_button");

downBtn.addEventListener("click", () => {
    const target = document.querySelector("#about");
    target.scrollIntoView({ behavior: 'smooth' });
})

//Side-Navigation

$(function () {

    var link = $('#navbar a.dot');
    link.on('click', function (e) {

        var target = $($(this).attr('href'));

        $('html, body').animate({
            scrollTop: target.offset().top
        }, 00);

        $(this).addClass('active');

        e.preventDefault();
    });

    $(window).on('scroll', function () {
        findPosition();
    });

    function findPosition() {
        $('section').each(function () {
            if (($(this).offset().top - $(window).scrollTop()) < 20) {
                link.removeClass('active');
                $('#navbar').find('[data-scroll="' + $(this).attr('id') + '"]').addClass('active');
            }
        });
    }

    findPosition();
});

// Scroll-Animation
window.sr = ScrollReveal();

sr.reveal('.animate-top', {
    origin: 'top',
    duration: 1000,
    distance: '25rem',
    delay: 300
});

sr.reveal('.animate-bottom', {
    origin: 'bottom',
    duration: 1000,
    distance: '25rem',
    delay: 600
});

sr.reveal('.animate-bottom-1', {
    origin: 'bottom',
    duration: 1000,
    distance: '5rem',
    opacity: 0,
    delay: 900
});

sr.reveal('.animate-bottom-card-1', {
    origin: 'bottom',
    duration: 1000,
    distance: '25rem',
    delay: 600
});

sr.reveal('.animate-bottom-card-2', {
    origin: 'bottom',
    duration: 1000,
    distance: '25rem',
    delay: 800
});

sr.reveal('.animate-bottom-card-3', {
    origin: 'bottom',
    duration: 1000,
    distance: '25rem',
    delay: 1000
});

sr.reveal('.animate-bottom-card-4', {
    origin: 'bottom',
    duration: 1000,
    distance: '25rem',
    delay: 1200
});

sr.reveal('.animate-left', {
    origin: 'left',
    duration: 1000,
    distance: '25rem',
    delay: 300
});

sr.reveal('.animate-right', {
    origin: 'right',
    duration: 1000,
    distance: '25rem',
    delay: 600
});

sr.reveal('.animate-top-1', {
    origin: 'top',
    duration: 1000,
    distance: '25rem',
    delay: 900
});

sr.reveal('.animate-top-3', {
    origin: 'top',
    duration: 1000,
    distance: '25rem',
    delay: 1500
});

sr.reveal('.animate-top-button', {
    origin: 'top',
    duration: 1000,
    distance: '10rem',
    delay: 400
});


sr.reveal('.animate-bottom-button', {
    origin: 'bottom',
    duration: 1000,
    distance: '25rem',
    delay: 800
});