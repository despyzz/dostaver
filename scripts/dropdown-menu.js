const showNav = document.getElementById('toggle-nav');
showNav.addEventListener('click', () => {
    toggleNav();
    document.body.style.overflow = 'hidden';
});

const hideNav = document.getElementById('close-dropdown-menu')
hideNav.addEventListener('click', () => {
    toggleNav();
    document.body.style.overflow = '';
});

function toggleNav() {
    let nav = document.querySelector('nav');
    nav.classList.toggle('active');
}