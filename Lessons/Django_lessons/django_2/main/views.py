from django.shortcuts import render
from .models import Page


def persons(request):
    persons_list = Page.objects.all()
    return render(request, "index.html", {"persons_list":persons_list})