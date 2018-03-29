from django.db import models


class Cities(models.Model):
    country = models.ForeignKey('CountryCode', on_delete=models.CASCADE)
    city = models.CharField("Название города", max_length=50)
    accent_city = models.CharField("Название города в этом городе", max_length=50)
    region = models.CharField("Регион", max_length=999, blank=True)
    population = models.BigIntegerField("Популяция", blank=True)
    latitude = models.FloatField("Долгота")
    longitude = models.FloatField("Широта")

    def __str__(self):
        return self.city


class CountryCode(models.Model):
    title = models.CharField("Код страны", max_length=3)

    def __str__(self):
        return self.title
