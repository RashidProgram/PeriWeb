from django.db import models

Kind = (
    ('h', "Хищник"),
    ('t', "Травоядное"),
    ('v', "Всеядное"),
)


class Animal(models.Model):
    name = models.CharField('Кличка', max_length=30)
    kind = models.CharField('Вид', choices=Kind, max_length=1)
    img = models.ImageField('Фото', upload_to="animals", blank=True)

    def get_img_url(self):
        return self.img.url if self.img else ""

    def __str__(self):
        return self.name