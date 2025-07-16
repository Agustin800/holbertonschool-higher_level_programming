const update = document.querySelector('#update_header');

update.addEventListener('click', function () {
    document.querySelector('header').textContent = 'New Header!!!'
});