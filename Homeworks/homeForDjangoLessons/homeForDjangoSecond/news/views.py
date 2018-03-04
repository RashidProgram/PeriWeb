from django.shortcuts import render
from .models import Article


def news_list(request):
    news = Article.objects.all()
    return render(request, "news.html", {'news': news})
