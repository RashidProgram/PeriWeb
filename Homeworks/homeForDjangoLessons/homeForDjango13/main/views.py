from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from users.models import User


class SecretView(LoginRequiredMixin, TemplateView):
    template_name = 'main/secret.html'


def home(request):
    return render(request, 'main/home.html', {'model': User})
