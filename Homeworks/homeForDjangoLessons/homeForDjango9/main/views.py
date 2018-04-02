from django.views.generic import DetailView, ListView
from .models import Cities


class CitiesListView(ListView):
    template_name = 'cities/list.html'
    context_object_name = 'cities'
    paginate_by = 100
    model = Cities


class CityDetailView(DetailView):
    template_name = 'cities/detail.html'
    context_object_name = 'city'
    model = Cities
