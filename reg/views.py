from django.shortcuts import render, redirect
from .models import reg
from .forms import regForm, StatusForm

def glavn(request):
    return render(request, 'reg/glavn.html', {'title': 'Главная страница'})

def regis(request):
    error = ''

    # если был отправлен запрос на создание фильтров
    selected_status = request.POST.get('status')
    projects = reg.objects.all()
    print(request.POST)
    if selected_status:
        dateReg = projects.filter(status=selected_status)
    else:
        dateReg = reg.objects.all()


    # если был запрос на создание нового проекта мы заполняем его в БД
    if request.method == 'POST':
        form = regForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.Responsible = request.user.get_full_name()
            form.save()
            form.numbers = form.id
            form.save()
            print(form.Responsible, form.numbers)
            return redirect('regis')
        else:
            error = 'Что то не так с запросом на создание проекта'

    # Сортировка только тех проектов, которые созданы активным пользователем
    for i in request.user.groups.values_list():
        if i[1] in ['Администраторы', 'Super_user']:
            dateReg = reg.objects.all()
            title = 'Список всех проектов'
        else:
            dateReg = projects.filter(Responsible=request.user.get_full_name())
            title = 'Список Ваших проектов'

    form = regForm()
    content = {
        'statuses': StatusForm,
        'title': title,
        'dateReg': dateReg,
        'form': form,
        'error': error,
        'title2': 'Регистрация нового проекта'
    }

    return render(request, 'reg/reg.html', content)

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