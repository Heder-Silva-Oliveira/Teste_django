from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return redirect('/agenda')


def login_user(request):
    render(request, 'login.html')


@login_required(login_url='/login/')
def lita_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos', evento}
    return render(request, 'agenda.html', dados)
