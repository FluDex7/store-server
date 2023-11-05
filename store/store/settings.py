"""
Django settings for store project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Содержит путь до проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Секретный ключ обеспечивает целостность передачи данных между серверами и между клиентами
SECRET_KEY = 'django-insecure-6)hy6ucn0czj&tol$ycci&22o2e59@9v_dn@en&xr$pj9w@uxw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Разрешенные домены, например: 'mysite.com' или '*' для всех доменов
ALLOWED_HOSTS = ['*']

DOMAIN_NAME = 'http://localhost:8000'

# Application definition
# Установленные приложения [users app & products app]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'products',  # добавление приложения
    'users',
]
# Промежуточные слои
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Расположение url-адресов
ROOT_URLCONF = 'store.urls'
# Отвечает за отображение шаблонов и их работу
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'products.context_processors.baskets',
            ],
        },
    },
]
# Расположение файла wsgi; wsgi и asgi нужны для deploy сервера на production
WSGI_APPLICATION = 'store.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# информация о том, какая база данных используется
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
# Валидация для паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },  # должна быть маленькая заглавная буква
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },  # минимум 8 символов
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },  # должен быть уникальным, должен совпадать "введите пароль" и "подтвердите пароль"
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },  # должна быть цифра (не точно)
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# Язык проекта
LANGUAGE_CODE = 'ru-ru'
# Тайм-зона
TIME_ZONE = 'UTC'
# Доп. поля для локализации (для перевода на языки)
USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# путь, где хранятся статические файлы (html, css, images, javascript)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # путь для папки с статическими файлами
]

# Настройки для работы с медиа-файлами
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# Поле по умолчанию (для работы с БД)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Users
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'  # Переадресация после входа в аккаунт
LOGOUT_REDIRECT_URL = '/'  # Переадресация после выхода с аккаунта

# sending emails
EMAIL_HOST = 'smtp.yandex.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'tes7server@yandex.ru'
EMAIL_HOST_PASSWORD = 'JRuY3Y-Pof'
EMAIL_USE_SSL = True
