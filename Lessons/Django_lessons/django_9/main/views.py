from django.views.generic import TemplateView, ListView, DetailView
from .models import Simple

class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = "home page"
        return context


class About(Home):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['phone'] = "8928432"
        return context


class SimpleListView(ListView):
    template_name = "queryset.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(title__icontains="s")
        return queryset


class SimpleDetailView(DetailView):
    template_name = "detail.html"
    object = Simple
