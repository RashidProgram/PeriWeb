from django.views.generic import TemplateView, ListView, DetailView
from .models import Animal


class IndexView(TemplateView):
    template_name = "index.html"


class AnimalListView(ListView):
    paginate_by = 2
    template_name = "animals.html"
    model = Animal


class AnimalDetailView(DetailView):
    template_name = "animal.html"
    model = Animal
