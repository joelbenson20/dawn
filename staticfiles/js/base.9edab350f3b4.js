const links = document.querySelectorAll('a.hyper-link');

links.forEach((link, index) => {
    link.innerHTML += `<sup><i class="fa-solid fa-up-right-from-square"></i></sup>`;
});