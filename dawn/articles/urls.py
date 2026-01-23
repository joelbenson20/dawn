from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>', views.article, name='article'),
]