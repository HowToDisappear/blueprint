
let divtxt = document.querySelector('#divtxt');
let inptxt = document.querySelector('#inptxt');
let form = document.querySelector('#form');
let cancel = document.querySelector('#cancel');
let submit = document.querySelector('#submit');
let user = document.querySelector('#user');

form.addEventListener('submit', function() {
    inptxt.value = divtxt.textContent;
    return true;
});

divtxt.addEventListener('input', function(e) {
    if (e.target.textContent.length === 0) {
        submit.disabled = true;
        submit.style.backgroundColor = '#999';
        submit.style.cursor = 'default';
    }
    else if (e.target.textContent.length > 280) {
        e.target.textContent = e.target.textContent.substring(0, 280);
    }
    else {
        submit.disabled = false;
        submit.style.backgroundColor = '#333333';
        submit.style.cursor = 'pointer';
    }
});

divtxt.addEventListener('focus', function() {
    if (!user.textContent) {
        window.location.replace('/accounts/login/')
    }
    cancel.style.display = 'block';
    submit.style.display = 'block';
});
cancel.addEventListener('click', function() {
    cancel.style.display = 'none';
    submit.style.display = 'none';
    divtxt.textContent = "";
    submit.style.backgroundColor = '#999';
    submit.style.cursor = 'default';
});

