$(".form").submit(function(e) {
    e.preventDefault(); // предотвращает отправку формы

    let form = $(this);
    let url = form.attr('action'); // получает URL из атрибута 'action' формы

    $.ajax({
        type: "POST",
        url: url,
        data: form.serialize(), // сериализует данные формы
        success: function(data)
        {
            let modalThanks = document.getElementById("thanks")
            modalThanks.classList.add('modal_active')
        },
        error: function()
        {
            alert("Произошла ошибка при отправке данных");
        }
    });
});