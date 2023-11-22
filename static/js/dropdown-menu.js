let showNav = document.getElementById('toggle-nav');
showNav.addEventListener('click', toggleNav);

let hideNav = document.getElementById('close-dropdown-menu')
hideNav.addEventListener('click', toggleNav)

function toggleNav() {
    let nav = document.querySelector('nav');
    nav.classList.toggle('active')
}