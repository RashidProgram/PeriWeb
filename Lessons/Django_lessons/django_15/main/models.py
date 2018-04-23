from django.db import models


class Person(models.Model):
    name = models.CharField('Имя', max_length=60)
    age = models.PositiveSmallIntegerField("Возраст")

    def __str__(self):
        return self.name