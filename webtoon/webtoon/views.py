from django.shortcuts import HttpResponse, render
from . import cr

def main(request):
    return render(request, "index.html")

def test(request):
    return HttpResponse("Hello World")

def webtoon(request):
    webtoons = cr.webtoon()
    context = {"webtoons" : webtoons}
    return render(request, "webtoon.html", context=context)