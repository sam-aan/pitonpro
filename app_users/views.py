from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from app_users.forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'

class AnotherLogoutView(LogoutView):
    next_page = '/'


def logout_view(request):
    logout(request)
    return HttpResponse('Пока!')

def login_view(request):
    if request.method == 'POST':    # для POST пытаемся аутентифицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Привет')
                else:
                    auth_form.add_error('__all__', 'Ошибка! нет такого пользователя!')
            else:
                auth_form.add_error('__all__', 'Ошибка! Неверно ввели данные!')
    else:   # для всех остальных запросов отображаем страничку для входа
        auth_form = AuthForm()
    content = {
        'form': auth_form,
        'title': 'Регистрация Пользователя',
    }
    return render(request, 'users/login.html', context=content)

