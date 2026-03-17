from hyper.templates.hyperrender_modules import image_module, hyper_link_module, hyper_modal_link_module
import re

def hyperrender(content, object=None):
    return re.sub(r'\((.*?)\)\[(.*?):(.*?)\]', lambda match: hyperrender_element(match, object), content)

def hyperrender_element(match_string, object):

    text = match_string.group(1)
    module = match_string.group(2)
    data = match_string.group(3)

    if (module == 'image'):
        try:
            image = object.images.get(slug=data)
            url = image.image.url
            caption = image.description
        
            return image_module % (url, caption)
        except:
            print('Error rendering content image with slug "%s"' % data)
            return     

    elif (module == 'fragment'):
        try:
            fragment = object.fragments.get(slug=data)
            return hyper_modal_link_module % (fragment.slug, text)
        except:
            print('Error rendering content fragment with slug "%s"' % data)
            return     
        
    elif (module == 'link'):
        url = data
        return hyper_link_module % (url, text)
        
    elif (module == 'dropcap'):
        return '<span class="dropcap">%s</span>' % text
    
    return