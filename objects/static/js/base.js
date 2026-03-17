const hyper_links = document.querySelectorAll('a.hyper-link');
const hyper_popups = document.querySelectorAll('.hyper-popup-link');
const hyper_window = document.getElementById('hyperWindow');

hyper_links.forEach((hyper_link, index) => {
    hyper_link.innerHTML += `<sup><i class="fa-solid fa-up-right-from-square"></i></sup>`;
});
hyper_popups.forEach((hyper_popup, index) => {
    hyper_popup.innerHTML += `<sup><i class="fa-solid fa-clone"></i></sup>`;
});

function createHyperPopup(hyper_popup_link) {
    const hyper_popup_modal = `
        <div class="hyper-popup col mx-auto my-auto align-center border-glow rounded p-3">
            <p class="hyper-exit-button text-glow float-end">&times;</p>
            <i class="fa-solid fa-clone text-left"></i>
            ${hyper_popup_link.dataset.hyperPopupContent}
        </div>
    `;

    hyper_window.innerHTML = hyper_popup_modal;
    hyper_window.style.display = 'flex';
};

function closeHyperWindow() {
    hyper_window.innerHTML = '';
    hyper_window.style.display = 'none';
}