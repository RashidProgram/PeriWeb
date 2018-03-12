from django.db import models


class Catalog(models.Model):
    title = models.CharField('Название каталога', max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталоги'
        verbose_name_plural = "Каталогов"


class Product(models.Model):
    title = models.CharField('Название продукта', max_length=100)
    slug = models.SlugField(max_length=100)
    company = models.CharField('Название компании', default=None, max_length=50)
    cost = models.FloatField("Цена", default=0.00)
    date = models.DateField(default="1970-01-01")
    catalog = models.ForeignKey(Catalog, verbose_name='Каталог', on_delete=models.CASCADE)
    weight = models.FloatField()

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товаров"

    def __str__(self):
        return self.title
