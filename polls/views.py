from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(request):
    return HttpResponse("Hello I am folling the right path of computer programming!")


