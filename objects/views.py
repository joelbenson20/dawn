from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import DawnObject, DawnArticle, DawnImage
import datetime


def object(request, model, year, month, day, slug):

    date = datetime.date(int(year), int(month), int(day))

    if model == 'dawnarticle':
        article = get_object_or_404(DawnArticle, publication_date=date, slug=slug, published=True)
        return render(request, 'article.html', context={'article': article})

    if model == 'dawnimage':
        image = get_object_or_404(DawnImage, publication_date=date, slug=slug, published=True)
        return render(request, 'image.html', context={'image': image})

    raise Http404()