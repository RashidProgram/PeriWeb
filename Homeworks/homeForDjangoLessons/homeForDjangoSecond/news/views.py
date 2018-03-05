from django.shortcuts import render
from .models import Article


def news_list(request, article_id=None):
    if article_id is None:
        news_detal = None
    else:
        news_detal = Article.objects.get(id=article_id)
    news = Article.objects.all()
    return render(request, "news.html", {'news': news, "news_detal": news_detal})
