const hamburger = document.querySelector('.hamburger');
const hamburgerLinks = document.querySelector('.hamburgerLinks');

hamburger.addEventListener('click', function () {
    hamburger.classList.toggle('active');
    hamburgerLinks.classList.toggle('active');
});


