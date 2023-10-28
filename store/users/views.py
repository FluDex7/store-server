from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse  # Принимает name=... и возвращает строку, по которому находиться адрес

from users.models import User
from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':  # Если пользователь отправляет данные со страницы
        form = UserLoginForm(data=request.POST)  # request.POST содержит данные с формы
        if form.is_valid():  # Проверка формы на валидацию
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) # Аутентификация пользователя
                                                                           # (проверяет есть ли он в БД)
            if user:  # Если пользователь существует, авторизоваться
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))  # Перенаправляет на главную страницу, если успешно
    else:  # Если пользователь запрашивает саму страницу
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    return render(request, 'users/register.html')
