from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from products.models import ProductCategory, Product, Basket  # Подключение таблиц(моделей) и последующая передача..
                                                      # ..в качестве аргумента
# Create your views here.
# здесь создаются функции(могут и классы) для отображения шаблонов приложения
# сленг: функции = контроллеры = вьюхи
# request - экземляр класса HttpRequest; в файле urls.py каждый контроллер передаётся ссылкой,
#           и в методе path вызывается контроллер с параметром request (запрос).



class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()  # Product.objects.all()
        category_id = self.kwargs.get('category_id')  # kwargs - словарик переданных данных; ключ должен совпадать с динамической переменной в URLS.py
                                                      # когда вызывается get для словарика, а такого ключа нет - то возвращается None
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()  # вызов родительского класса перед добавлением своих параметров
        context['title'] = 'Store - Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context


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