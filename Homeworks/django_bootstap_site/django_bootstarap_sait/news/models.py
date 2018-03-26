from django.db import models
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField

Tags = (
    ('о', 'Опасность'),
    ('g', 'Государство'),
    ('se', 'Сенсация'),
    ('sr', 'Срочные'),
)


class News(models.Model):
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("Слуг", max_length=50)
    date = models.DateField("Дата", default=now)
    img = models.ImageField("Изображение", upload_to='news', blank=True, null=True)
    content = RichTextUploadingField('Контент', default='Статья к новости еще не создана')
    tags = models.CharField("Теги", choices=Tags, blank=True, max_length=2)

    def get_img_url(self):
        if self.img:
            return self.img.url
        return ''

    def __str__(self):
        return self.name
