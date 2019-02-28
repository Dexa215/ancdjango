from django.urls import path
from . import views

urlpatterns = [
    path('',             views.index,                        name="index"),
    path('home/',        views.HomeView.as_view(),           name="indexhome"),
    path('elencosoci/',  views.ElencoSociView.as_view(),     name="elencosoci"),

]
