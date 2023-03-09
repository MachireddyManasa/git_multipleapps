from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def mother(request):
    return HttpResponse('mother is a housewife')

def father(request):
    return HttpResponse('father is a farmer')

def manasa(request):
    return HttpResponse('I am learning about django')
