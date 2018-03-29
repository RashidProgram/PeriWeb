from django.db import models


class Page(models.Model):
    title = models.CharField("ЗАГОЛОВОК", max_length=200)
    about = models.TextField("КОНТЕНТ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"