from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateField('День рождения')
    avatar = ImageField(upload_to='photo/', blank=True)
    is_chickcirik = models.BooleanField('чикчирик?', default=False)
    REQUIRED_FIELDS = ['email', 'birthday', 'is_chickcirik']
