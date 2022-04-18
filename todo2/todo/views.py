from django.shortcuts import render, redirect, HttpResponse
from .models import todo

def index(request):
    return redirect("main/")

def main(request):
    if request.method == "GET":
        data = todo.objects.all()
        content = {
            "data" : data
        }
        return render(request, "index.html", content)

    elif request.method == "POST":
        recode = todo()
        recode.name = request.POST.get("name")
        recode.save()
        return redirect("/")

def delete(request, id):
    data = todo.objects.get(id = id)
    data.delete()
    return redirect("/")