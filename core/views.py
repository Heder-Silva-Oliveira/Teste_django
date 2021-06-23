from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requet):
    return HttpResponse('Hello Word')