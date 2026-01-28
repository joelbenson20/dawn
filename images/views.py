from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Image
import datetime

def image(request, year, month, day, slug):

    date = datetime.date(int(year), int(month), int(day))

    image = get_object_or_404(Image, publication_date=date, slug=slug, published=True)

    context = {'image': image}

    return render(request, 'image.html', context=context)

