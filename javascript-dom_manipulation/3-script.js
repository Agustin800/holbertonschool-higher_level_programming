if (document.querySelector('header').getAttribute('class') != 'red' &&
    document.querySelector('header').getAttribute('class') != 'green') {
    document.querySelector('header').setAttribute('class', 'green');
}

document.querySelector('#toggle_header').addEventListener('click', function () {
    if (document.querySelector('header').getAttribute('class') == 'green') {
        document.querySelector('header').setAttribute('class', 'red');
    }
    else {
        document.querySelector('header').setAttribute('class', 'green');
    }
});