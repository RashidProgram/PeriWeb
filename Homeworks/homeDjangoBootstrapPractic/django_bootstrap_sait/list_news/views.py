from django.shortcuts import render
from .models import News


def list_news(request):
    return render(request, 'list_news.html', {'news': News.objects.all()})


def detail_news(request, slug):
    return render(request, 'detail_news.html', {'news': News.objects.get(slug=slug)})
