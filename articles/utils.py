
from articles.templates.modules.hyper import content_image_module, link_module
import re

def hyper_render(match_string, article):

    text = match_string.group(1)
    module = match_string.group(2)
    data = match_string.group(3)

    print(match_string[3])

    if (module == 'image'):
        try:
            content_image = article.content_images.get(slug=data)

            url = content_image.image.url
            caption = content_image.caption

            return content_image_module % (url, caption)
        except:
            return
        
    elif (module == 'link'):
        try:
            url = data
            return link_module % (url, text)
        except:
            return
        
    return
