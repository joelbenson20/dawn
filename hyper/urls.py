from django.urls import path
from . import views

urlpatterns = [
    path('<str:module>/<int:id>/', views.hyper),
]