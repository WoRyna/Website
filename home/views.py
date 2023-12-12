from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World !!!</h1>")

def cat(request, cat_slug):
    return HttpResponse(f"<h2>Another page</h2><p>{cat_slug}</p>")
"""
def archive(request, year):
    return HttpResponse(f"<h1>Archive</h1><p>{year}</p>")
"""
