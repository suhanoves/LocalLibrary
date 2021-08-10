import datetime

from django import forms
from django.core.exceptions import ValidationError


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text='Enter a date between now and 4 weeks (default 3).')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError('Дата не может быть в прошлом')

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Книгу нельзя выдавать больше чем на 4 недели')

        return data
