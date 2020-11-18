
// highlight current nav section
let sectionsNames = ['art', 'events', 'yourart'];
let url = document.URL;
let sectionsNodes = document.querySelectorAll('.header-nav-section');
for (let i = 0; i < 3; i++) {
    if (window.location.pathname.split("/")[1] === sectionsNames[i]) {
        sectionsNodes[i].classList.toggle('active');
    }
}

// hide header-nav and footer at login-registration page
let logreg = ['login', 'register', 'submit',]
for (let i = 0; i < logreg.length; i++) {
    if (url.includes(logreg[i])) {
        document.querySelectorAll('.header-nav')[0].style.display = 'none';
        document.querySelectorAll('main.content')[0].style.paddingTop = '65px';
        document.querySelectorAll('.footer')[0].style.display = 'none';
        document.querySelector('.user').style.display = 'none';
    }
}
