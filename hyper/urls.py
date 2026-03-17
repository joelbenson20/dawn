from django.urls import path
from . import views

urlpatterns = [
    path('<str:module>/<str:slug>/', views.hyper),
]