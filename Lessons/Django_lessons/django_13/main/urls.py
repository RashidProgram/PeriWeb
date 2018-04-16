from django.urls import path
from django.views.generic import TemplateView
from .views import SecretView

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/home.html'), name='home'),
    path('secret/', SecretView.as_view(), name='secret'),
]
