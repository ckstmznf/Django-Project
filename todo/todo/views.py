from django.shortcuts import render, HttpResponse, redirect
from .models import todo

def test(request):
    return render(request, "test.html")

def main(request):
    if request.method == "GET":
        data = todo.objects.all()
        context = {
            "data": data,
        }
        return render(request, "index.html", context)
    elif request.method == "POST":
        recode = todo()
        recode.name = request.POST.get("name")
        recode.save()
        return redirect("/")


def delete(request):
    id = request.GET.get("id")
    todo.objects.get(id=id).delete()
    return redirect("/")