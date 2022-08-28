from .models import reg
from django.forms import ModelForm, TextInput

class regForm(ModelForm):
    class Meta:
        model = reg
        fields = ['NameProg', 'Customer_company', 'Adres_obj']
        #exclude = ['Responsible']
        widgets = {
            'NameProg': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование проекта'
                }),
            'Customer_company': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ИНН контрагента',
                'maxlength': '10'   # Ограничим ввод на странице 10 символами
                }),
            'Adres_obj': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес объекта (Страна, Город, Улица, №Дома)'
                })
                }