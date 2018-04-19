from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        field_classes = {'username': UsernameField}
        fields = ("username", "first_name", "last_name", "email", 'avatar', 'birthday', 'is_chickcirik')
