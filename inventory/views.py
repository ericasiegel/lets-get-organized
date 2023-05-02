from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def object_list(request):
    return HttpResponse('objects list here')
