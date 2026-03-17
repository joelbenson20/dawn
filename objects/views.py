from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import DawnArticle, DawnImage
import datetime
from itertools import chain
from operator import attrgetter

def index(request):

    dawn_articles = DawnArticle.objects.filter(published=True)
    dawn_images = DawnImage.objects.filter(published=True)

    posts = list(chain(dawn_articles, dawn_images))
    posts.sort(key=attrgetter('publication_date'), reverse=True)

    context = {'posts': posts}

    return render(request, 'index.html', context=context)

def object(request, model, year, month, day, slug):

    date = datetime.date(int(year), int(month), int(day))

    if model == 'dawnarticle':
        article = get_object_or_404(DawnArticle, publication_date=date, slug=slug, published=True)
        return render(request, 'article.html', context={'article': article})

    if model == 'dawnimage':
        image = get_object_or_404(DawnImage, publication_date=date, slug=slug, published=True)
        return render(request, 'image.html', context={'image': image})

    raise Http404()