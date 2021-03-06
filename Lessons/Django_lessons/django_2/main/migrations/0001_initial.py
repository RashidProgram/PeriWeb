# Generated by Django 2.0.2 on 2018-02-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='имя ')),
                ('surname', models.CharField(max_length=210, verbose_name='фамилия')),
                ('about', models.TextField(verbose_name='о себе ')),
                ('mass', models.PositiveSmallIntegerField(verbose_name='Вес')),
                ('birth', models.DateField(verbose_name='Дата рожденния')),
            ],
            options={
                'verbose_name': 'Персона',
                'verbose_name_plural': 'Персоны',
                'ordering': ['name'],
            },
        ),
    ]
