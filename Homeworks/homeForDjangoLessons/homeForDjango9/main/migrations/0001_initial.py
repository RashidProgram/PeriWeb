# Generated by Django 2.0.2 on 2018-03-29 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Название города')),
                ('accent_city', models.CharField(max_length=50, verbose_name='Название города в этом городе')),
                ('region', models.PositiveIntegerField(blank=True, verbose_name='Регион')),
                ('population', models.BigIntegerField(verbose_name='Популяция')),
                ('latitude', models.FloatField(verbose_name='Долгота')),
                ('longitude', models.FloatField(verbose_name='Широта')),
            ],
        ),
        migrations.CreateModel(
            name='CountryCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3, verbose_name='Код страны')),
            ],
        ),
        migrations.AddField(
            model_name='cities',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.CountryCode'),
        ),
    ]
