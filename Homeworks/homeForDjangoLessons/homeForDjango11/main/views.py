from django.shortcuts import render, reverse
from .forms import ZayavkaForm, OdzivForm
from django.views.generic import CreateView
from .models import ZayavkaModel


def otziv(request):
    is_valid = False
    form = OdzivForm(initial={'name': 'Ваше имя'})
    if request.method == 'POST':
        form = OdzivForm(request.POST)
        if form.is_valid():
            form.send_mail()
            is_valid = True
    return render(request, 'odziv.html', {'form': form, 'is_valid': is_valid})


class ZayavkaCreateView(CreateView):
    form_class = ZayavkaForm
    template_name = 'zayavka.html'
    queryset = ZayavkaModel.objects.all()

    def get_success_url(self):
        return reverse('odziv')
