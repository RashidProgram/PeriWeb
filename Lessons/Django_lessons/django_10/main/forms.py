from django import forms


class TestForm(forms.Form):
    name = forms.CharField(max_length=255, help_text="Твое имя ")
    birth = forms.DateField(help_text="Твой день рождения ")
    age = forms.IntegerField(min_value=0, max_value=255, help_text="Твой возраст ")
