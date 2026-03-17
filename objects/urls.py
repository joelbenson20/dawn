from django.urls import path
from . import views

urlpatterns = [
    path('<str:model>/<int:year>/<int:month>/<int:day>/<str:slug>', views.object, name='object'),
]