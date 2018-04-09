from django.db import models


class ZayavkaModel(models.Model):
    name = models.CharField("ФИО", max_length=200)
    age = models.IntegerField('Возраст')
    email = models.EmailField('Mail', max_length=500)

    def __str__(self):
        return self.name
