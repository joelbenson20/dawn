from hyper.templates.hyperrender_modules import content_image_module, hyper_link_module, hyper_popup_link_module
import re

def hyperrender(content, object=None):
    return re.sub(r'\((.*?)\)\[(.*?):(.*?)\]', lambda match: hyperrender_element(match, object), content)

def hyperrender_element(match_string, object):

    text = match_string.group(1)
    module = match_string.group(2)
    data = match_string.group(3)

    if (module == 'image'):
        try:
            content_image = object.content_images.get(slug=data)
            url = content_image.image.url
            caption = content_image.description
        
            return content_image_module % (url, caption)
        except:
            print('Error rendering content image with slug "%s"' % data)
            return          
        
    elif (module == 'link'):
        url = data
        return hyper_link_module % (url, text)
    
    elif (module == 'popup'):
        content = data
        return hyper_popup_link_module % (content, text)
        
    elif (module == 'dropcap'):
        return '<span class="dropcap">%s</span>' % text
    
    return