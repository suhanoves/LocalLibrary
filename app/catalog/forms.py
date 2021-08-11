import datetime

from django import forms
from django.core.exceptions import ValidationError

from catalog import models


class RenewBookModelForm(forms.ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        if data < datetime.date.today():
            raise ValidationError('Дата не может быть в прошлом')

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Книгу нельзя выдавать больше чем на 4 недели')

        return data

    class Meta:
        model = models.BookInstance
        fields = ['due_back', ]
        labels = {'due_back': 'Renewal date', }
        help_texts = {'due_back': 'Enter a date between now and 4 weeks (default 2).', }
