from django.shortcuts import render, redirect
from .models import reg
from .forms import regForm

def glavn(request):
    return render(request, 'reg/glavn.html', {'title': 'Главная страница'})

def regis(request):
    dateReg = reg.objects.all()
    return render(request, 'reg/reg.html', {'title': 'Зарегистрированные проекты', 'dateReg': dateReg})

def inreg(request):
    error = ''

    if request.method == 'POST':
        form = regForm(request.POST)

        if form.is_valid():
            form.save()
            print('Нажали конпкуууууууу!!!')
            return redirect('home')
        else:
            error = 'Чет ты натыкал???'

    form = regForm()
    content = {
        'form': form,
        'error': error,
        'title': 'Регистрация'
    }
    return render(request, 'reg/inreg.html', content)