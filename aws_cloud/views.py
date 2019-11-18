from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>AWS Cloud</h1>')

def about(request):
    return HttpResponse('<h1>AWS Cloud About page</h1>')