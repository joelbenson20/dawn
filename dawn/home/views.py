from django.shortcuts import render
from articles.models import Article
from images.models import Image
from itertools import chain
from operator import attrgetter

def index(request):

    articles = Article.objects.filter(published=True)
    images = Image.objects.filter(published=True)

    posts = list(chain(articles, images))
    posts.sort(key=attrgetter('publication_date'), reverse=True)

    context = {'posts': posts}

    return render(request, 'index.html', context=context)