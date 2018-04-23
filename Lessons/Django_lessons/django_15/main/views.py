from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .forms import PersonModelForm


class Home(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            message = 'Вы отправили сооющение:"'
            message += request.GET['message']
            return JsonResponse({'message': message})
        else:
            return super().get(request, *args, **kwargs)


def ajax_user(request):
    message = 'Вы отправили сооющение:"'
    message += request.GET['message']
    return JsonResponse({'message': message})


class SendView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            message = 'Вы отправили сооющение:"'
            message += request.GET['message']
            return render(request, 'send_ajax.html', {'message':message})
        else:
            return super().get(request, *args, **kwargs)


class SendFormView(TemplateView):
    template_name = 'formsend.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = PersonModelForm()
        return context

    def post(self, *args, **kwargs):
        form = PersonModelForm(self.request.POST)
        if form.is_valid():
            form.save()
            message = 'Данные сохранены'
        else:
            message = 'Неверные данные'
        if self.request.is_ajax():
            return JsonResponse({'message': message})
        else:
            return render(self.request, 'send_ajax.html', {'message': message})
