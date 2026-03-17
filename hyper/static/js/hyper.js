const hyper_links = document.querySelectorAll('a.hyper-link');
const hyper_modal_links = document.querySelectorAll('.hyper-modal-link');
const hyper_window = document.getElementById('hyperWindow');

hyper_links.forEach((hyper_link, index) => {
    hyper_link.innerHTML += `<sup><i class="fa-solid fa-up-right-from-square"></i></sup>`;
});
hyper_modal_links.forEach((hyper_modal_link, index) => {
    hyper_modal_link.innerHTML += `<sup><i class="fa-solid fa-clone"></i></sup>`;
});

function openHyper(hyper_button) {

    const module = 'fragment';
    const slug = hyper_button.dataset.hyperWindowContent;
    const url = `/hyper/${module}/${slug}/`;

    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return response.text();
        })
        .then(content => {
            const hyper_modal = `
                <div class="hyper-modal col mx-auto my-auto align-center border-glow rounded p-3">
                    <p class="hyper-exit-button text-glow float-end">&times;</p>
                    <i class="fa-solid fa-clone text-left"></i>
                    ${content}
                </div>
            `;
            hyper_window.innerHTML = hyper_modal;
            hyper_window.style.display = 'flex';
        })
        .catch(err => console.error('Hyper fetch error:', err));
};

function closeHyperWindow() {
    hyper_window.innerHTML = '';
    hyper_window.style.display = 'none';
}

console.log('Hello from hyper.js!');