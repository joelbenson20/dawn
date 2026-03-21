image_module = """
    <figure class="w-75 mx-auto my-5">
        <img class="img-fluid content-image" src="%s"><br>
        <small class="content-image-caption  pt-2">%s</small>
    </figure>
"""

hyper_link_module = """
    <a class="hyper-link" href="%s" target="_blank">%s<sup><i class="fa-solid fa-arrow-up-right-from-square"></i></sup></a>
"""

hyper_frame_link_module = """
    <span class="hyper-frame-link" onclick="openHyperFrame(this)" data-hyper-frame-id="%s">%s<sup><i class="fa-solid fa-clone"></i></sup></span>
"""