from django.shortcuts import render
from django.http import HttpResponse, Http404
from hyper.models import Fragment

def hyper(request, module, id):

    if (module == "fragment"):
        try:
            fragment = Fragment.objects.get(id=id)
            return HttpResponse(fragment.rendered_content)
        except Fragment.DoesNotExist:
            raise Http404("Fragment not found")

    raise Http404("Module not found")
