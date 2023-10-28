from django.contrib.auth.forms import AuthenticationForm

# Подключение формы к модели(таблице) User
from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')