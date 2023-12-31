from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisements
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'font-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if '?' in title[0]:
            raise ValidationError('Заголовок не может начинаться с вопросительного знака!')
        return title