from django.shortcuts import render

from products.models import ProductCategory, Product  # Подключение таблиц(моделей) и последующая передача..
                                                      # ..в качестве аргумента
# Create your views here.
# здесь создаются функции(могут и классы) для отображения шаблонов приложения
# сленг: функции = контроллеры = вьюхи
# request - экземляр класса HttpRequest; в файле urls.py каждый контроллер передаётся ссылкой,
#           и в методе path вызывается контроллер с параметром request (запрос).


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.object.all(),  # products = [<QuerySet [<Product: ... | Category: ...>]>,
                                                       # <QuerySet [<Product: ... | Category: ...>]>,
                                                       # ...]
        'categories': ProductCategory.object.all(),  # categories = [<QuerySet ['Одежда']>, <QuerySet ['Обувь']>]
    }
    return render(request, 'products/products.html', context=context)
