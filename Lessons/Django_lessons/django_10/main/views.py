from django.shortcuts import render, reverse
from .forms import TestForm, NewTestForm
from .models import Test
from django.views.generic import DeleteView, UpdateView, CreateView, ListView


def home(request):
    is_valid = False
    form = TestForm(initial={'name': 'Ваше имя'})
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            birth = form.cleaned_data.get('birth')
            Test.objects.create(name=name, age=age, birth=birth)
            is_valid = True
    return render(request, 'home.html', {'form': form, 'is_valid': is_valid})

def new_home(request):
    is_valid = False
    form = TestForm(initial={'name': 'Ваше имя'})
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            is_valid = True
    return render(request, 'home.html', {'form': form, 'is_valid': is_valid})


class PeriCreateView(CreateView):
    form_class = NewTestForm
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('home')

class PeriUpdateView(UpdateView):
    form_class = NewTestForm
    template_name = 'update.html'
    queryset = Test.objects.all()

    def get_success_url(self):
        return reverse('home')

class PeriListView(ListView):
    model = Test
    template_name = "list.html"


class PeriDeleteView(DeleteView):
    form_class = NewTestForm
    template_name = 'update.html'
    queryset = Test.objects.all()

    def get_success_url(self):
        return reverse('home')
# def home(request):

#     if request.method == 'POST':
#         form = TestForm(request.POST)
#         if form.is_valid():
#             return render(request, 'home.html', {'is_valid': True})
#         else:
#             return render(request, 'home.html', {'form': form})
#     return render(request, 'home.html', {'form': TestForm()})
