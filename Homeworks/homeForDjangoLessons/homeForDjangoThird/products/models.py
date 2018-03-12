from django.db import models


class Catalog(models.Model):
    title = models.CharField('Название каталога', max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталоги'
        verbose_name_plural = "Каталогов"


class Products(models.Model):
    title = models.CharField('Название продукта', max_length=100)
    slug = models.SlugField(max_length=100)
    company = models.CharField('Название компании', default=None, max_length=50)
    cost = models.DecimalField("Цена", decimal_places=2, max_digits=5, blank=True)
    date = models.DateField(default="1970-01-01")
    catalog = models.ForeignKey(Catalog, verbose_name='Каталог', on_delete=models.CASCADE)
    weight = models.FloatField()
    image = models.ImageField("Фото", null=True, blank=True, upload_to="products/")
    is_import = models.BooleanField("Оригинал", default=False)
    url = models.URLField("Сайт производителя")
    email = models.EmailField("Маил")

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товаров"

    def __str__(self):
        return self.title


class Options(models.Model):
    title = models.CharField('Title', max_length=128)
    value = models.CharField('Value', max_length=1028)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
