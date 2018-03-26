from django.views.generic import DetailView, ListView
from .models import News


class NewsListView(ListView):
    template_name = "list_news.html"
    model = News
    context_object_name = 'news'


class NewsDetailView(DetailView):
    template_name = "detail_news.html"
    model = News

