# Generated by Django 2.0.3 on 2018-03-25 10:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180325_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Статья к новости еще не создана', verbose_name='Контент'),
        ),
    ]