from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dwarika(request):
    return HttpResponse('<h1>hey my name is dwarika<h1/>')