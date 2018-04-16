from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SecretView(LoginRequiredMixin, TemplateView):
    template_name = 'main/secret.html'
