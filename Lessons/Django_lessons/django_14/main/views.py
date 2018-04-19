from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse


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