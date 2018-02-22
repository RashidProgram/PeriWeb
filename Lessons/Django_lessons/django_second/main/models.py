from django.db import models


class Person(models.Model):
    name = models.CharField("имя ", max_length=200)
    surname = models.CharField("фамилия", max_length=210)
    about = models.TextField("о себе ")
    mass = models.PositiveSmallIntegerField("Вес")
    birth = models.DateField("Дата рожденния")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"
        ordering = ["name"]
