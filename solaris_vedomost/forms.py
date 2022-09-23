from .models import SolVed
from django.forms import ModelForm, TextInput, FileInput
from django import forms


class solvedom(ModelForm):
    class Meta:
        file = forms.FileField()
        model = SolVed
        fields = ['NomProj', 'NomZak', 'PromPlosh', 'uploadedFile']
        widgets = {'NomZak': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер заказа'}),
        }
