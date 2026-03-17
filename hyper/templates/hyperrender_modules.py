content_image_module = """
    <figure class="w-75 mx-auto my-5">
        <img class="img-fluid content-image" src="%s">
        <small class="content-image-caption  pt-2">%s</small>
    </figure>
"""

hyper_link_module = """
    <a class="hyper-link" href="%s" target="_blank">%s</a>
"""

hyper_popup_link_module = """
    <span class="hyper-popup-link" onclick="createHyperPopup(this)" data-hyper-popup-content="<p>%s</p>">%s</span>
"""