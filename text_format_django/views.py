from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'Sherry', 'place': 'Earth'}
    return render(request, 'index.html', params)


def removepunc(request):
    return HttpResponse("<h1>Removed Punctuation</h1> <a href='/'>Back</a>")


def capfirst(request):
    return HttpResponse("<h1>Capitalized First Letter</h1> <a href='/'>Back</a>")


def newlineremove(request):
    return HttpResponse("<h1>New Line Removed</h1> <a href='/'>Back</a>")


def spaceremove(request):
    return HttpResponse("<h1>Extra Spaces Removed</h1> <a href='/'>Back</a>")


def charcount(request):
    return HttpResponse("<h1>Character Counted</h1> <a href='/'>Back</a>")