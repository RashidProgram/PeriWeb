from django.contrib.auth.views import LoginView
from django.urls import path

from users.views import UserCreateView, logout_view

app_name = 'users'

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]