let z_index = 3;

function openHyperModal(hyper_button) {

    const hyper_window = document.getElementById('hyperWindow');
    const module = 'fragment';
    const slug = hyper_button.dataset.hyperModalContent;
    const url = `/hyper/${module}/${slug}/`;

    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return response.text();
        })
        .then(content => {
            const hyper_modal = `
                <div class="hyper-modal-backdrop position-fixed top-0 start-0 w-100 h-100 d-flex" style="z-index: ${z_index};" onClick="closeHyperModal(this)">
                    <div class="hyper-modal col mx-auto my-auto align-center border-glow rounded p-3" style="z-index: ${z_index++};" onClick="event.stopPropagation()">
                        <p class="hyper-exit-button text-glow float-end" onClick="exitHyperModal(this)">&times;</p>
                        <i class="fa-solid fa-clone text-left"></i>
                        ${content}
                    </div>
                </div>
            `;
            hyper_window.insertAdjacentHTML('beforeend', hyper_modal);
            console.log(z_index);
        })
        .catch(err => console.error('Hyper fetch error:', err));
};

function closeHyperModal(hyper_modal) {
    console.log('closed!');
    hyper_modal.remove();
}

function exitHyperModal(exit_button) {
    const hyper_modal = exit_button.closest('.hyper-modal-backdrop');
    hyper_modal.remove();
}