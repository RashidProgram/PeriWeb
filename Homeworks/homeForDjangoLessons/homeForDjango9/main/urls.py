from django.urls import path
from .views import CityDetailView, CitiesListView

app_name = 'cities'

urlpatterns = [
    path('/', CitiesListView.as_view(), name="list"),
    path('detail/<int:pk>', CityDetailView.as_view(), name="detail"),
]
