from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Article
import datetime

def articles(request):

    articles = Article.objects.filter(published=True).order_by('-publication_date')

    context = {'articles': articles}

    return render(request, 'articles.html', context=context)


def article(request, year, month, day, slug):

    date = datetime.date(int(year), int(month), int(day))

    article = get_object_or_404(Article, publication_date=date, slug=slug, published=True)

    context = {'article': article}

    return render(request, 'article.html', context=context)
