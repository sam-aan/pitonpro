from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from .models import reg
from .forms import regForm

def glavn(request):
    return render(request, 'reg/glavn.html', {'title': 'Главная страница'})


def regis(request):
    error = ''
    # Сортировка только тех проектов, которые созданы активным пользователем
    # для Админа
    if request.user.has_perm('reg.delete_reg'):
        dateReg = reg.objects.all()
        title = 'Список всех проектов'
        nameGroup = True
    # для продавцов
    elif request.user.has_perm('reg.add_reg'):
        dateReg = reg.objects.filter(Responsible=request.user.get_full_name())
        title = 'Список Ваших проектов'
        nameGroup = True
    elif request.user.has_perm('reg.view_reg'):
        dateReg = reg.objects.all()
        title = 'Список всех проектов'
        nameGroup = False
    else:
        raise PermissionDenied


    # если был запрос на создание нового проекта, мы заполняем его в базу данных
    if request.method == 'POST':
        print('POST', request.POST)
        form = regForm(request.POST)

        # Проверяем что нам вернулось с post запросом со страницы
        if 'new_sdelka' in request.POST:
            if form.is_valid():
                form = form.save(commit=False)
                form.Responsible = request.user.get_full_name()
                form.save()
                form.numbers = form.id
                form.save()
                return redirect('regis')
            else:
                error = 'Что то не так с запросом на создание проекта'
        # Если post запрос связан с выбранной из карточек сделкой
        elif 'sdelka' in request.POST:
            return redirect('sdelka', request.POST['sdelka'])
        # Если post запрос связан с сортировкой списка карточек сделок
        elif 'sortirovka' in request.POST:
            selected_sorting = request.POST['sortirovka']
            if selected_sorting in ['все']:
                if request.user.has_perm('reg.add_reg'):
                    dateReg = reg.objects.filter(Responsible=request.user.get_full_name())
                else:
                    dateReg = reg.objects.all()
            else:
                dateReg = dateReg.filter(Status=selected_sorting)
        else:
            error = 'POST запрос с ошибкой!'

    form = regForm()
    content = {
        'nameGroup': nameGroup,
        'title': title,
        'dateReg': dateReg,
        'form': form,
        'error': error,
        'title2': 'Регистрация нового проекта'
    }

    return render(request, 'reg/reg.html', content)

def inreg(request):
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

def sdelka(request, sdelka_id):
    obj = reg.objects.get(id=sdelka_id)
    title = 'Сделка№ ' + obj.numbers + ' ' + obj.NameProg
    date_born = obj.Date_born
    content = {
        'title': title,
        'sdelka_id': sdelka_id,
        'date_born': date_born,
    }
    return render(request, 'reg/sdelka.html', content)