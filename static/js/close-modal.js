let modalWindows = document.querySelectorAll('.modal');
modalWindows.forEach(function (modalWindow) {
    modalWindow.addEventListener('click', function (event) {
        if (event.target === modalWindow) {
            closeModal();
        }
    })
    let closeButton = modalWindow.querySelector('.close-icon');
    closeButton.addEventListener('click', closeModal);

    function closeModal() {
        modalWindow.classList.toggle('modal_active');
    }
})