from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect


class UserCreateView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'create.html'
    success_url = '/'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
