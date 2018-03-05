from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    name = models.CharField("Название", max_length=70)
    news_info = models.CharField("Описание", max_length=300)
    news_details = RichTextUploadingField("подробности")

    def __str__(self):
        return self.name
