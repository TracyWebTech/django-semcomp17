from django.http import HttpResponse
from django.shortcuts import render

from .models import Palestra


def hello_world(request):
    return HttpResponse('Hello World!! =)')


def lista_palestras(request):
    palestras = Palestra.objects.all()
    context = {
        'palestras': palestras,
    }
    return render(request, 'palestras.html', context)

