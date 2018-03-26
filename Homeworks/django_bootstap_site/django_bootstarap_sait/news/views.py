from django.views.generic import TemplateView, ListView, DetailView
from .models import News


class HomeView(TemplateView):
    template_name = 'index.html'


class NewsListView(ListView):
    template_name = 'news.html'
    model = News
    context_object_name = 'news'
    paginate_by = 2


class NewsDetailView(DetailView):
    model = News
    template_name = 'article.html'
    context_object_name = 'article'
