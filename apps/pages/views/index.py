from django.contrib import messages
from django.shortcuts import render


def index(request):
    messages.success(request, 'Esta é uma mensagem de sucesso!')

    return render(request, 'index.html')
