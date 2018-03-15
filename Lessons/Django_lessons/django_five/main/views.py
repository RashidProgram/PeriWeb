from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'index.html', context)


def second(request, name):
    return render(request, 'hello.html', {"name": name})
