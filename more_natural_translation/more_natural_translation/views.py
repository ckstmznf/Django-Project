from django.shortcuts import render, HttpResponse, redirect
from .translation import *

def main(request):
    return render(request, "index.html")

def reslut(request):
    text = request.POST.get("text")
    source_lang = request.POST.get("sL")
    if source_lang == "ko":
        target_lang = "en"
    else:
        target_lang = "ko"

    data = all(source_lang, target_lang, text)
    data["text"] = data["text"].split("\n")
    data["direct"]["text"] = data["direct"]["text"].split("\n")
    data["indirect"]["text"] = data["indirect"]["text"].split("\n")


    return render(request, "reslut.html", context=data)