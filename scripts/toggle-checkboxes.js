let checkboxContainers = document.querySelectorAll('.checkbox-container');

checkboxContainers.forEach(function (checkboxContainer) {
    checkboxContainer.addEventListener('click', function () {
        let checkIcon = checkboxContainer.querySelector('.toggle-checkbox');
        let checkInput = checkboxContainer.querySelector('.checkbox-input');

        if (checkIcon.style.opacity === '0' || checkIcon.style.opacity === '') {
            checkIcon.style.opacity = '1';
            checkInput.value = 'true';
        } else {
            checkIcon.style.opacity = '0';
            checkInput.value = 'false';
        }
    });
});
