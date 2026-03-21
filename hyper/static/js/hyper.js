let z_index = 3;

function openHyperFrame(hyper_button) {

    const hyper_window = document.getElementById('hyperWindow');
    const module = 'fragment';
    const slug = hyper_button.dataset.hyperFrameId;
    const url = `/hyper/${module}/${slug}/`;

    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return response.text();
        })
        .then(content => {
            const hyper_frame = `
                <div class="hyper-frame-backdrop position-fixed top-0 start-0 w-100 h-100 d-flex" style="z-index: ${z_index};" onClick="closeHyperFrame(this)">
                    <div class="hyper-frame col mx-auto my-auto border-glow rounded p-3" style="z-index: ${z_index++};" onClick="event.stopPropagation()">
                        <p class="hyper-exit-button text-glow float-end" onClick="exitHyperFrame(this)">&times;</p>
                        <i class="fa-solid fa-clone text-left"></i>
                        ${content}
                    </div>
                </div>
            `;
            hyper_window.insertAdjacentHTML('beforeend', hyper_frame);
            console.log(z_index);
        })
        .catch(err => console.error('Hyper fetch error:', err));
};

function closeHyperFrame(hyper_frame) {
    console.log('closed!');
    hyper_frame.remove();
}

function exitHyperFrame(exit_button) {
    const hyper_frame = exit_button.closest('.hyper-frame-backdrop');
    hyper_frame.remove();
}