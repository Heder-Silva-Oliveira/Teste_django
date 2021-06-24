from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(requet, nome):
    return HttpResponse('<h1>Hello Word {}</h1>'.format(nome))
