from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexapp1, name='index'),
]