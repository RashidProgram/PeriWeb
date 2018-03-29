from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField("Название", max_length=180)
    slug = models.SlugField("СЛУГ")
    img = models.ImageField("Фото", blank=True, upload_to='news')
    small_content = models.CharField("Краткое содержание", max_length=500)
    detail_content = RichTextUploadingField("Полное содержание")

    def get_img(self):
        return self.img.url if self.img.url else ""

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
