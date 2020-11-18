
window.addEventListener('load', expColl);

// ------- content expand-collapse -------
function expColl() {
    let descrPar = document.querySelectorAll('.descr-par')[0];
    let descrBtn = document.querySelectorAll('.descr-btn')[0];
    if (descrPar.clientHeight > 200) {
        descrPar.classList.toggle('short');
        descrBtn.style.display = 'block';

        descrBtn.addEventListener('click', function(e) {
            let x = window.pageXOffset;
            let y = window.pageYOffset;
            descrPar.classList.toggle('short');
            if (descrPar.classList.contains('short')) {
                descrBtn.textContent = 'Expand';
            }
            else {
                window.scroll(x, y);
                descrBtn.textContent = 'Collapse';
            }
        });
    }

}


// ------- slider -------
var windW;
var cardW;
var cards = document.querySelectorAll('.card');
var transX = 0;

function cardWidthCalc() {
    this.windW = window.innerWidth;
    if (this.cards.length >= 3) {
        if (this.windW < 1440) {
            this.cardW = (this.windW - 100 - 40) / 3;
        }
        else {
            this.cardW = (1440 - 100 - 40) / 3;
        }
        for (let i = 0; i < this.cards.length; i++) {
            this.cards[i].style.width = this.cardW + 'px';
        }
    }
    else {
        for (let i = 0; i < this.cards.length; i++) {
            this.cards[i].style.width = 35 + '%';
        }
    }
}

window.addEventListener('load', cardWidthCalc);
window.addEventListener('resize', cardWidthCalc);


function buttons () {
    if (this.cards.length > 3) {
        let boxW = this.cards.length * (this.cardW + 20) - 100 - 20;
        if ( Math.abs(transX)+(this.cardW*3+40) > boxW ) {
            document.querySelector('.rarr').style.display = 'none';
        }
        else {
            document.querySelector('.rarr').style.display = 'block';
        }
        if ( Math.abs(transX)-(this.cardW*3+40) < 0 ) {
            document.querySelector('.larr').style.display = 'none';
        }
        else {
            document.querySelector('.larr').style.display = 'block';
        }
    }
    else {
        document.querySelector('.rarr').style.display = 'none';
        document.querySelector('.larr').style.display = 'none';
    }
}

window.addEventListener('load', buttons);

function shift(e, direction) {
    if (direction === 'l') {
        this.transX += (this.cardW*3+60)
        document.querySelector('.artworks').style.transform = 'translateX('+this.transX+'px)';
    }
    else {
        this.transX -= (this.cardW*3+60)
        document.querySelector('.artworks').style.transform = 'translateX('+this.transX+'px)';
    }
    this.buttons();
}

let larr = document.querySelector('.larr');
let rarr = document.querySelector('.rarr');
larr.addEventListener('click', function (e) { shift(e, direction='l'); });
rarr.addEventListener('click', function (e) { shift(e, direction='r'); });