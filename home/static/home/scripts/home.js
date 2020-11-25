
var intervId;
var slideNo = 1;
var slides = document.querySelectorAll('.slider li');
var controls = document.querySelectorAll('.slider-controls button');
var playback = document.querySelector('#playback');
var play = document.querySelector('#play');
var pause = document.querySelector('#pause');

function init() {
    change();
    intervId = window.setInterval(change, 6000);
    pause.style.display = 'block';
    play.style.display = 'none';
}
function term() {
    clearInterval(intervId);
    intervId = false;
    pause.style.display = 'none';
    play.style.display = 'block';
}

function change() {
    slides.forEach(slide => {
        slide.classList.add('opaque');
        slide.style.zIndex = '5';
    });
    controls.forEach(control => {
        control.classList.remove('active');
        control.firstElementChild.style.color = 'white';
    });
    visible = document.querySelector(`#slide-${slideNo}`);
    visible.classList.remove('opaque');
    visible.style.zIndex = '10';
    controls[`${slideNo}`].classList.add('active');
    controls[`${slideNo}`].firstElementChild.style.color = 'black';

    if (slideNo == 5) {
        slideNo = 1;
    } else {
        slideNo = slideNo + 1;
    }

}

window.addEventListener('load', init);


for (let i = 1; i <= 5; i++) {
    controls[i].addEventListener('click', function(e) {
        manual(e, i);
    });
}

playback.addEventListener('click', function() {
    intervId ? term() : init();
});

function manual(e, No) {
    term();
    slideNo = No;
    change();
}



// var sl1 = document.querySelector('#one');
// var sl2 = document.querySelector('#two');
// var sl3 = document.querySelector('#three');
// var sl4 = document.querySelector('#four');
// var sl5 = document.querySelector('#five');
// var playback = document.querySelector('#playback');

// sl1.addEventListener('click', function(e) {manual(e, 1);});
// sl2.addEventListener('click', function(e) {manual(e, 2);});
// sl3.addEventListener('click', function(e) {manual(e, 3);});
// sl4.addEventListener('click', function(e) {manual(e, 4);});
// sl5.addEventListener('click', function(e) {manual(e, 5);});
// playback.addEventListener('click', init);

// function manual(e, No) {
//     term();
//     slideNo = No;
//     change();
// }