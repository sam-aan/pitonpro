from .models import reg
from django.forms import ModelForm, TextInput, Select, Textarea

class regForm(ModelForm):
    class Meta:
        model = reg
        fields = ['NameProg', 'Adres_obj']
        widgets = {
            'NameProg': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование проекта'
                }),
            'Adres_obj': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес объекта (Страна, Город, Улица, №Дома)'
                })
                }

class StatusForm(ModelForm):
    class Meta:
        model = reg
        fields = ['Status']
        widgets = {
            'Status': Select(attrs={
                'class': 'select',  # Можете задать класс по вашему усмотрению
                'value': Select,
            })
        }