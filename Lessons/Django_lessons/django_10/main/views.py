from django.shortcuts import render
from .forms import TestForm


def home(request):
    form = TestForm()
    is_valid = False
    if request.method == "GET":
        form = TestForm(request.GET)
        if form.is_valid():
            cdata = form.cleaned_data
            name = cdata.get('name')
            birth = cdata.get('birth')
            age = cdata.get('age')

            is_valid = True
    return render(request, "index.html", {'form': form, 'is_valid': is_valid})
