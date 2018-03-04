from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    name = models.CharField(max_length=30)
    news_list = models.CharField(max_length=100)
    news_details = RichTextUploadingField()

    def __str__(self):
        return self.name
