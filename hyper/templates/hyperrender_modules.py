image_module = """
    <figure class="w-75 mx-auto my-5">
        <img class="img-fluid content-image" src="%s"><br>
        <small class="content-image-caption  pt-2">%s</small>
    </figure>
"""

hyper_link_module = """
    <a class="hyper-link" href="%s" target="_blank">%s<sup><i class="fa-solid fa-arrow-up-right-from-square"></i></sup></a>
"""

hyper_modal_link_module = """
    <span class="hyper-modal-link" onclick="openHyperModal(this)" data-hyper-modal-content="%s">%s<sup><i class="fa-solid fa-clone"></i></sup></span>
"""