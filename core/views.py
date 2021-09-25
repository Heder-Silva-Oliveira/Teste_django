from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return redirect('/ola_django')

@login_required()
def lita_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos', evento}
    return render(request, 'agenda.html', dados)
