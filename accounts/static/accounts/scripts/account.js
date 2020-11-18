
let fnameEdit = document.querySelector('#fname-edit');
let lnameEdit = document.querySelector('#lname-edit');

let fnameCancel = document.querySelector('.cancel.fname');
let lnameCancel = document.querySelector('.cancel.lname');

let fnameInput = document.querySelector('#id_first_name');
let lnameInput = document.querySelector('#id_last_name');



fnameEdit.addEventListener('click', function() {
    document.querySelector('.data-form.fname').firstElementChild.nextElementSibling.value = document.querySelector('.data-db.fname').lastElementChild.textContent;
    document.querySelector('.data-db.fname').style.display = 'none';
    document.querySelector('.data-form.fname').style.display = 'block';
});
fnameCancel.addEventListener('click', function() {
    document.querySelector('.data-form.fname').firstElementChild.nextElementSibling.value = '';
    document.querySelector('.data-db.fname').style.display = 'block';
    document.querySelector('.data-form.fname').style.display = 'none';
});
fnameInput.addEventListener('input', function(e) {
    let save = document.querySelector('#save-fname');
    if (e.target.value.length === 0) {
        save.disabled = true;
        save.style.backgroundColor = '#999';
        save.style.cursor = 'default';
    }
    else {
        save.disabled = false;
        save.style.backgroundColor = '#333333';
        save.style.cursor = 'pointer';
    }
});

lnameEdit.addEventListener('click', function() {
    document.querySelector('.data-form.lname').firstElementChild.nextElementSibling.value = document.querySelector('.data-db.lname').lastElementChild.textContent;
    document.querySelector('.data-db.lname').style.display = 'none';
    document.querySelector('.data-form.lname').style.display = 'block';
});
lnameCancel.addEventListener('click', function() {
    document.querySelector('.data-form.lname').firstElementChild.nextElementSibling.value = '';
    document.querySelector('.data-db.lname').style.display = 'block';
    document.querySelector('.data-form.lname').style.display = 'none';
});
lnameInput.addEventListener('input', function(e) {
    let save = document.querySelector('#save-lname');
    if (e.target.value.length === 0) {
        save.disabled = true;
        save.style.backgroundColor = '#999';
        save.style.cursor = 'default';
    }
    else {
        save.disabled = false;
        save.style.backgroundColor = '#333333';
        save.style.cursor = 'pointer';
    }
});




var form = document.querySelector('form');


let avInput = document.querySelector('#image');
let avBtn = document.querySelector('#avatar-btn');
let avAction = document.querySelector('#av_action');
let avDelete = document.querySelector('#delete>div');

window.addEventListener('load', function() {
    avInput.style.display = 'none';
    if (avatar && area) {
        avBtn.textContent = 'Upload';
    }
    if (avatar && !area) {
        avDelete.style.display = 'block';
        avBtn.textContent = 'Change';
    }
});
avBtn.addEventListener('click', function() {
    if (avatar) {
        if (!area) {
            avAction.value = 'replace';
            avInput.click();
        }
        else {
            // added upload
            avAction.value = 'upload';
            form.requestSubmit();
        }
    }
    else {
        avInput.click();
    }
});
avInput.addEventListener('input', function() {
    // added upload
    avAction.value = 'upload';
    form.requestSubmit();
});


avDelete.addEventListener('click', function() {
    avAction.value = 'delete';
    form.requestSubmit();
});






// crop --------------------------------->

var avatar = document.querySelector('#avatar');
window.addEventListener('load', function() {
    if (avatar && area) {
        initPic();
    }
});

var area = document.querySelector('#area');
var crop_params, avW, avH, avX, avY, minside;
function initPic() {
    // area = document.querySelector('#area');
    crop_params = document.querySelector('#crop_params');
    avW = avatar.getBoundingClientRect().width;
    avH = avatar.getBoundingClientRect().height;
    avX = avatar.getBoundingClientRect().x;
    avY = avatar.getBoundingClientRect().y;
    // setting crop side
    minside = Math.min(avW, avH);
    area.style.width = `${minside - 4}px`;
    area.style.height = `${minside - 4}px`;
    // setting crop position
    if (avW >= avH) {
        area.style.left = `${avX + (avW - minside)/2 + 2}px`;
        area.style.top = `${avY + 2}px`;
    } else {
        area.style.top = `${avY + (avH - minside)/2 + 2}px`;
        area.style.left = `${avX + 2}px`;
    }
    // cropping area dynamics
    area.addEventListener('mousedown', function(e) {
        initResize(e);
    });
    form.addEventListener('submit', cropParams);
}


function cropParams() {
    // setting crop_params input field values for PIL
    let factorX, factorY, left, upper, right, lower;
    factorX = avatar.naturalWidth/avW;
    factorY = avatar.naturalHeight/avH;
    left = (parseInt(area.style.left, 10) - avX)*factorX;
    upper = (parseInt(area.style.top, 10) - avY)*factorY;
    right = left + (parseInt(area.style.width, 10))*factorX;
    lower = upper + (parseInt(area.style.height, 10))*factorY;
    crop_params.value = `[${left},${upper},${right},${lower}]`;
}



// cropping area dynamics
const BORDER = 8;
var corner = '';
var startX, startY, startWidth, startHeight, startPosLeft, startPosTop;

function initResize(e) {
    let x = e.offsetX;
    let y = e.offsetY;
    if (x <= BORDER) {
        if (y <= BORDER) {
            corner = 'topLeft';
        } else if (y >= parseInt(window.getComputedStyle(area).height, 10) - BORDER) {
            corner = 'bottomLeft';
        }
    } else if (x >= parseInt(window.getComputedStyle(area).width, 10) - BORDER) {
        if (y <= BORDER) {
            corner = 'topRight';
        } else if (y >= parseInt(window.getComputedStyle(area).height, 10) - BORDER) {
            corner = 'bottomRight';
        }
    }
    if (corner) {
        console.log(corner);
        startResize(e);
    } else {
        startMove(e);
    }
}

function startResize(e) {
    startX = e.clientX;
    startY = e.clientY;
    startWidth = parseInt(window.getComputedStyle(area).width, 10);
    startHeight = parseInt(window.getComputedStyle(area).height, 10);
    window.addEventListener('mousemove', resize);
    window.addEventListener('mouseup', stopResize);
}
function stopResize(e) {
    window.removeEventListener('mousemove', resize);
    window.removeEventListener('mouseup', stopResize);
    corner = '';
}
function resize(e) {
    if (corner === 'bottomRight') {
        let square = `${Math.max(startWidth + e.clientX - startX, startHeight + e.clientY - startY)}px`;
        area.style.width = square;
        area.style.height = square;
    }
}

function startMove(e) {
    startX = e.clientX;
    startY = e.clientY;
    startPosTop = parseInt(window.getComputedStyle(area).top, 10);
    startPosLeft = parseInt(window.getComputedStyle(area).left, 10);
    window.addEventListener('mousemove', move);
    window.addEventListener('mouseup', stopMove);
}
function stopMove(e) {
    window.removeEventListener('mousemove', move);
    window.removeEventListener('mouseup', stopMove);
}
function move(e) {
    var newPosTop = startPosTop + e.clientY - startY;
    var newPosLeft = startPosLeft + e.clientX - startX;
    if (newPosTop < avY) {
        newPosTop = avY;
    } else if (newPosTop > (avY + avH - parseInt(area.style.height, 10))) {
        newPosTop = (avY + avH - parseInt(area.style.height, 10));
    }
    if (newPosLeft < avX) {
        newPosLeft = avX;
    } else if (newPosLeft > (avX + avW - parseInt(area.style.width, 10))) {
        newPosLeft = (avX + avW - parseInt(area.style.width, 10));
    }
    area.style.top = `${newPosTop}px`;
    area.style.left = `${newPosLeft}px`;
}
