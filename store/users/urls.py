from django.urls import path

from users.views import login, register  # Подключение контроллеров файла views.py приложения products

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]