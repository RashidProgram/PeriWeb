from django.contrib import admin
from django.urls import path
from main.views import UserCreateView
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from main.views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('singup', UserCreateView.as_view(), name="create_user"),
    path('', lambda request: render(request, 'index.html', {}), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),
]
