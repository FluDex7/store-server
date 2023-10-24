from django.shortcuts import render

# Create your views here.
# здесь создаются функции(могут и классы) для отображения шаблонов приложения
# сленг: функции = контроллеры = вьюхи
# request - экземляр класса HttpRequest; в файле urls.py каждый контроллер передаётся ссылкой,
#           и в методе path вызывается контроллер с параметром request (запрос).
def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')
