from .models import reg
from django.forms import ModelForm, TextInput

class regForm(ModelForm):
    class Meta:
        model = reg
        fields = ['nombers', 'NameProg']
        widgets = {
            'nombers': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование проекта'
                }),
            'NameProg': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер проекта'
                }),
            'Status': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите статус'
                })
                }