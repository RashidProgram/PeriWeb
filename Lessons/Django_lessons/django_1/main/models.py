from django.db import models


class Page(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Контент")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страницу"
        verbose_name_plural = "Страницы"
