from django.shortcuts import render
from .models import Person


def persons(request):
    persons_list = Person.objects.all()
    return render(request, "index.html", {"persons_list":persons_list})