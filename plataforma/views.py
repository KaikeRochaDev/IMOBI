from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Imovei, Cidade

@login_required(login_url='/auth/logar/')
def home(request):
    imoveis = Imovei.objects.all()
    cidades = Cidade.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})