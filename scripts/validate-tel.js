let forms = document.querySelectorAll('form');

forms.forEach(function (form) {
    let telInput = form.querySelector('.form__tel');
    let checkboxContainer = form.querySelector('.checkbox-container');
    let submitButton = form.querySelector('.form__callback');

    submitButton.disabled = true;

    telInput.addEventListener('input', updateButtonState);
    checkboxContainer.addEventListener('click', updateButtonState)

    function updateButtonState() {
        let checkboxInput = checkboxContainer.querySelector('.checkbox-input')

        let phoneNumber = telInput.value;
        let isCheckboxChecked = checkboxInput.value === 'true';
        let isValidNumber = validatePhoneNumber(phoneNumber);

        submitButton.disabled = !(isValidNumber && isCheckboxChecked);
    }
});

function validatePhoneNumber(phoneNumber) {
    return /\+7 \(\d{3}\) \d{3} \d{2} \d{2}/.test(phoneNumber);
}