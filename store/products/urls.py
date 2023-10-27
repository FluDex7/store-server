from django.urls import path

from products.views import products  # Подключение контроллеров файла views.py приложения products

app_name = 'products'

urlpatterns = [
    path('', products, name='index')
]

