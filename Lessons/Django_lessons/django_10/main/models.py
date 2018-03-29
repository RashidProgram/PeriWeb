from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=255, help_text="Твое имя ")
    birth = models.DateField(help_text="Твой день рождения ")
    age = models.IntegerField(min_value=0, max_value=255, help_text="Твой возраст ")
