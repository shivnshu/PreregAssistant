from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(requests):
    return HttpResponse("Welcome to assistant!")
