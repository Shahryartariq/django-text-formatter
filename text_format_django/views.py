from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>HOME</h1>")


def removepunc(request):
    return HttpResponse("<h1>Removed Punctuation</h1>")


def capfirst(request):
    return HttpResponse("<h1>Capitalized First Letter</h1>")


def newlineremove(request):
    return HttpResponse("<h1>New Line Removed</h1>")


def spaceremove(request):
    return HttpResponse("<h1>Extra Spaces Removed</h1>")


def charcount(request):
    return HttpResponse("<h1>Character Counted</h1>")
