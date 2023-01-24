from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse('Olá, você está no cadastro')

def logar(request):
    return HttpResponse('olá, você esta no logar')
