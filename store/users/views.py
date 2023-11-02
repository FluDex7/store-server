from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy  # Принимает name=... и возвращает строку, по которому находиться адрес
from django.views.generic.edit import CreateView, UpdateView

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


def login(request):
    if request.method == 'POST':  # Если пользователь отправляет данные со страницы
        form = UserLoginForm(data=request.POST)  # request.POST содержит данные с формы
        if form.is_valid():  # Проверка формы на валидацию
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # Аутентификация пользователя
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


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Store - Регистрация'
        return context


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Store - Личный кабинет'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     context = {
#         'title': 'Store - Профиль',
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user),
#     }
#     return render(request, 'users/profile.html', context)


# def register(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Поздравляем! Вы успешно зарегестрировались!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/register.html', context)
