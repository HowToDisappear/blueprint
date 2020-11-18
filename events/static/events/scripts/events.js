let etypeEls = document.getElementsByName('etype');
let etypes = document.getElementById('etypes');
let form = document.querySelector('.filters');
let button = document.querySelector('.button');


function apply() {
    let etypeVals = "";
    for (let i = 0; i < etypeEls.length; i++) {
        if (etypeEls[i].checked) {
            etypeVals = etypeVals + etypeEls[i].value + ',';
            // etypeEls[i].checked = false;
        }
    }
    etypes.value = etypeVals.slice(0,-1);
}

button.addEventListener('click', function() {
    apply();
    form.requestSubmit();
})