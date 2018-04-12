from django import forms
from .models import ZayavkaModel
from django.core.mail import send_mail, mail_admins
from homeForDjango11.settings import DEFAULT_FROM_EMAIL


class OdzivForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=500)
    text = forms.CharField(max_length=1000)

    def send_mail(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        text = self.cleaned_data.get('text')
        subject = 'Новый отзыв'
        message = '''Отзыв от {0}:
        {1}
        email: {2}'''.format(name, text, email)
        mail_admins(subject, message, )


class ZayavkaForm(forms.ModelForm):
    class Meta:
        model = ZayavkaModel
        fields = ['name', 'age', 'email']

    def save(self, commit=True):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        subject = 'Ваша заявка принята'
        message = "{0} Заявка принята на рассмотрение".format(name)
        send_mail(subject, message, from_email=DEFAULT_FROM_EMAIL, recipient_list=[email])
        return super().save(commit)

