from django.shortcuts import render
from django.http import HttpResponse, Http404
from hyper.models import Fragment

def hyper(request, module, slug):

    print(f"Module: {module}, Slug: {slug}")

    if (module == "fragment"):
        try:
            fragment = Fragment.objects.get(slug=slug)
            return HttpResponse(fragment.content)
        except Fragment.DoesNotExist:
            raise Http404("Fragment not found")

    raise Http404("Module not found")
