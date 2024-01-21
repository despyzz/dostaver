window.onscroll = function toggleScrollToTopButton() {
    const button = document.getElementById("scrollToTopButton");
    if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
        button.classList.add("visible");
        button.classList.remove("hidden")
    } else {
        button.classList.add("hidden")
        button.classList.remove("visible");
    }
}

function scrollToTop() {
    const scrollStep = -60; // Размер каждого шага прокрутки
    const scrollInterval = 10; // Интервал времени между шагами (увеличьте для более медленной прокрутки)

    const scrollToTop = () => {
        if (document.body.scrollTop > 0 || document.documentElement.scrollTop > 0) {
            window.scrollBy(0, scrollStep);
            setTimeout(scrollToTop, scrollInterval);
        }
    };
    scrollToTop();
}
