from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from .models import Socio
                            ###, Tessera, Rts

def index(request):
    print("tento di aprire index html...")
    return HttpResponse("Hello, world. You're at the core index.")

class HomeView(ListView):
    queryset = Socio.objects.all()
    template_name = 'core/homepage.html'
    context_object_name = "lista_soci"


class ElencoSociView(ListView):
    queryset = Socio.objects.raw('SELECT * FROM core_socio')
    template_name = 'core/elencosoci.html'
    context_object_name = "lista_soci"