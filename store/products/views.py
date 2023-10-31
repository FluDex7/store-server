from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from products.models import ProductCategory, Product, Basket  # Подключение таблиц(моделей) и последующая передача..
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


def products(request, category_id = None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Store - Каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),  # categories = [<QuerySet ['Одежда']>, <QuerySet ['Обувь']>]
    }
    return render(request, 'products/products.html', context=context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])  # возврат пользователя на эту же страницу


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])