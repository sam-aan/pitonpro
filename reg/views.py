from django.shortcuts import render, redirect
from .models import reg
from .forms import regForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime


def glavn(request):
    return render(request, 'reg/glavn.html', {'title': 'Главная страница'})

def regis(request):
    dateReg = reg.objects.all()
    return render(request, 'reg/reg.html', {'title': 'Зарегистрированные проекты', 'dateReg': dateReg})

def inreg(request, data=None):
    error = ''

    if request.method == 'POST':
        form = regForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.Responsible = request.user.get_full_name()
            form.save()
            form.numbers = form.id
            form.save()
            return redirect('regis')
        else:
            error = 'Чет ты натыкал???'

    form = regForm()
    content = {
        'form': form,
        'error': error,
        'title': 'Регистрация'
    }
    return render(request, 'reg/inreg.html', content)