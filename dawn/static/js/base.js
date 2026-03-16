let hyper_links = document.querySelectorAll('a.hyper-link');
let hyper_popups = document.querySelectorAll('.hyper-popup');

hyper_links.forEach((hyper_link, index) => {
    hyper_link.innerHTML += `<sup><i class="fa-solid fa-up-right-from-square"></i></sup>`;
});
hyper_popups.forEach((hyper_popup, index) => {

    hyper_popup.innerHTML += `<sup><i class="fa-solid fa-clone"></i></sup>`;
});

function showPopup(hyper_popup) {
    console.log('Clicked!');
};
