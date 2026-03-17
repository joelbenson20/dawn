from django.shortcuts import render
from objects.models import DawnArticle, DawnImage
from itertools import chain
from operator import attrgetter

def index(request):

    dawn_articles = DawnArticle.objects.filter(published=True)
    dawn_images = DawnImage.objects.filter(published=True)

    posts = list(chain(dawn_articles, dawn_images))
    posts.sort(key=attrgetter('publication_date'), reverse=True)

    context = {'posts': posts}

    return render(request, 'index.html', context=context)