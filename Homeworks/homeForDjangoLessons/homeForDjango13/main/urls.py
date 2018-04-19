from django.urls import path
from .views import SecretView, home

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('secret/', SecretView.as_view(), name='secret'),
]
