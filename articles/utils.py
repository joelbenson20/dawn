content_image_html = """
    <figure class="w-75 mx-auto my-5">
        <img class="img-fluid content-image" src="%s">
        <small class="content-image-caption  pt-2">%s</small>
    </figure>"""

def embed_image(match_string, article):
    try:
        image_number = int(match_string.group(1))
        content_image = article.content_images.all().order_by('slug')[image_number]

        url = content_image.image.url
        caption = content_image.caption

        return content_image_html % (url, caption)
    except:
        return ""
