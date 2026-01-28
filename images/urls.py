from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<str:slug>', views.image, name='image'),
]