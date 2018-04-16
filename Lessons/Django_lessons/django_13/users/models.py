from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from stdimage import StdImageField
from django.utils.translation import gettext_lazy as _


@admin.register(UserAdmin)
class User(models.Model):
    birthday = models.DateField('День рождения')
    avatar = StdImageField(upload_to='path/to/img',
                           variations={'thumbnail': {'width': 100, 'height': 75}},
                           blank=True)
    is_chickcirik = models.BooleanField('чикчирик?', default=False)
    REQUIRED_FIELDS = ['email', 'birthday', 'is_chickcirik']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )