from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField("Название", max_length=180)
    slug = models.SlugField("СЛУГ")
    small_content = RichTextUploadingField("Краткое содержание")
    deteil_content = RichTextUploadingField("Полное содержание")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
