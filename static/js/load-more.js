let loadMoreButton = document.getElementById('load-more-button');
loadMoreButton.addEventListener('click', function () {

    let hiddenBlocks = document.querySelectorAll('.hidden');
    hiddenBlocks.forEach(function (hiddenBlock) {
        hiddenBlock.classList.remove('hidden')
    });

    loadMoreButton.style.display = 'none';
});