"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Подключение медиа-файлов
from django.conf.urls.static import static
from django.conf import settings  # Так подтягиваются все настройки (в отличие от from store import settings)

from products.views import index  # Подключение контроллеров файла views.py приложения products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # передача контроллера осущесвтляется по ссылке(без скобок)
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users'))
]

# На локальном уровне
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
