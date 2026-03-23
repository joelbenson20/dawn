from hyper.templates.hyperrender_modules import hyper_img_module, hyper_a_module, hyper_frame_link_module
import bs4
import re

def hyperrender_content(object):

    soup = bs4.BeautifulSoup(object.content, 'html.parser')

    # Render drop caps
    for element in soup.find_all('hyper-cap'):
        try:
            text = element.text
            element.replace_with(bs4.BeautifulSoup('<span class="hyper-cap">%s</span>' % text, 'html.parser'))
        except:
            print('Error rendering content drop cap.')

    # Render hyper-a elements
    for element in soup.find_all('hyper-a'):
        try:
            href = element.get('href')
            text = element.text
            element.replace_with(bs4.BeautifulSoup(hyper_a_module % (href, text), 'html.parser'))
        except:
            print('Error rendering content link.')

    # Render hyper-img elements
    for element in soup.find_all('hyper-img'):
        try:
            id = element['data-id']
            image = object.images.get(id=id)
            url = image.image.url
            caption = image.description
            element.replace_with(bs4.BeautifulSoup(hyper_img_module % (url, caption), 'html.parser'))
        except:
            print('Error rendering content image.')

    # Render hyper-frame-link elements
    for element in sorted(soup.find_all('hyper-frame'), key=lambda x: len(list(x.parents)), reverse=True):
        if (element.has_attr('data-id')):
            try:
                id = element['data-id']
                text = element.text
                element.replace_with(bs4.BeautifulSoup(hyper_frame_link_module % (id, text), 'html.parser'))
            except:
                print('Error rendering content fragment.')

    return soup.prettify()

def hyperrender_element(match_string, object):

    text = match_string.group(1)
    module = match_string.group(2)
    data = match_string.group(3)

    if (module == 'image'):
        try:
            image = object.images.get(slug=data)
            url = image.image.url
            caption = image.description
        
            return hyper_img_module % (url, caption)
        except:
            print('Error rendering content image with slug "%s"' % data)
            return     

    elif (module == 'fragment'):
        try:
            fragment = object.fragments.get(id=data)
            return hyper_frame_link_module % (fragment.id, text)
        except:
            print('Error rendering content fragment with id "%s"' % data)
            return     
        
    elif (module == 'link'):
        url = data
        return hyper_a_module % (url, text)
        
    elif (module == 'dropcap'):
        return '<span class="dropcap">%s</span>' % text
    
    return