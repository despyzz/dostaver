$(".form").submit(function(e) {
    e.preventDefault();
    const modalThanks = document.getElementById("thanks");
    modalThanks.classList.add('modal_active');
    document.body.style.overflow = 'hidden';
});