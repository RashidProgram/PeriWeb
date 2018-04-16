from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect, reverse
from django.views.generic import CreateView

from .forms import MyUserCreationForm


class UserCreateView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'users/create.html'

    def get_success_url(self):
        return reverse("users:login")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
