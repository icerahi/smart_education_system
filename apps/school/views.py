from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def school(requests):
    return HttpResponse("this is school")
