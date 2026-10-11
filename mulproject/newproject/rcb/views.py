from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def captain(request):
    return HttpResponse('<h1>king virat is a good captain</h1>')