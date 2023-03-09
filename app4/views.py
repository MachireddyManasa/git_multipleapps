from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def manasa(request):
    return HttpResponse('I am learning about django')

def siri(request):
    return HttpResponse('siri and manasa are best friends')
