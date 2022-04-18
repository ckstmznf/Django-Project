from django.shortcuts import render, HttpResponse
from .naver_news_Wordcloud import *

def test(request):
    return HttpResponse("<h1>Hello World</h1>")

def main(request):
    return render(request, "index.html")


def topic(request):
    data = get_news_topics()
    content = {"data" : data}
    return render(request, "topic.html", content)

def WordCloud(request):
    list = naver_news_all()
    # list = get_news_topics()
    content = {"list" : list}
    return render(request, "wordcloud.html", content)