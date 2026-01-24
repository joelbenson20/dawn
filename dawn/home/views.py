from django.shortcuts import render
from articles.models import Article

def index(request):

    articles = Article.objects.filter(published=True).order_by('-publication_date')

    context = {'articles': articles}

    return render(request, 'index.html', context=context)