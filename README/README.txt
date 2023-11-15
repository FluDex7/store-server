TODO:-----------------------------------------------------FAQ-----------------------------------------------------------
########################################################################################################################
########################################################################################################################
###################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##########################
##################$ THIS WILL BE PLACED USEFUL LINKS TO DOCUMENTATION OF SOME MODULE OR APP $###########################
###################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##########################
########################################################################################################################
########################################################################################################################
------------------------------------------------------------------------------------------------------------------------

QuerySet - https://docs.djangoproject.com/en/4.2/ref/models/querysets/

Pagination - https://docs.djangoproject.com/en/4.2/topics/pagination/

Class-based views - https://docs.djangoproject.com/en/4.2/ref/class-based-views/

Model fields - https://docs.djangoproject.com/en/4.2/ref/models/fields/

------------------------------------------------------------------------------------------------------------------------

1. Сравнение локальной разработкой и разработкой, которая идёт на production:
local:
-исключительно на локальном компьютере или совместном проекте

* База данных: db.sqlite3
* deploy: 127.0.0.1:8000
* доступ: всем разработчикам проекта
* DEBUG: True

production:
-опубликованный на некоторый домен проект, с которым могут работать клиенты

* База данных: PostgreSQL
* deploy: mysite.com
* доступ: все пользователи
* DEBUG: False

2. Архитектуру БД следует продумать с самого начала!
-на основе архитектуры БД строят проект,
также помогает определить какие приложения будут в проекте.

для данного проекта(картинка архитектуры в файле architecture.png):
* таблица для пользователя(регистрация, вход, профиль)
* информация о товарах(название, цена, описание)
* таблица для категорий
* корзина товаров

3. Как работает Django(картинка в файле how_django_work.png):
HTTP Request(запрос) -> urls.py(проверка на определённый адрес) -> wiews.py
(определённого контроллера/представления) -> HTTP Response (HTML) (ответ сайта)
также к wiews.py добавляются статические файлы templates и таблицы model.py

4. url tags используют имена, которые указываются в файле urls.py

5. Типы для полей таблиц/моделей - https://docs.djangoproject.com/en/4.2/ref/models/fields/
Чтобы перенести структуру таблиц(моделей) на SQL --> надо сделать миграцию
Миграция - перенос структуры модели на структуру БД
Команды:
makemigrations - созданий новых миграций (создаёт структуру,
                 подготавливает файл чтобы таблицы создались в БД)
migrate - применение миграций (создание таблицы в БД)

QuerrySet - набор запросов, который представляет собой набор объектов из базы данных
Методы QuerrySet:
НазваниеКласса.object.______
.get() - Возвращает объект из БД (Например: ProductCategory.object.get(1) - вернёт объект с ID == 1)
.create() - Создаёт объект из БД (Например: ProductCategory.object.create(name='Обувь') - создает объект с полем
                                 name = 'Обувь' и пустым описанием(description), сразу записывается в БД,
                                 поэтому сохранять методом .save() не нужно)
.all() - Возвращает список объектов таблицы из БД
.filter() - Возвращает список объектов, подходящих под условие (Например: ProductCategory.object.filter(...
                                                                ...description=None - вернёт ...
                                                                ...<QuerySet [<ProductCategory: Обувь>]>)
Подробнее: https://docs.djangoproject.com/en/4.2/ref/models/querysets/

Обычно изображения загружают из-вне на сервер (не хранятся на статике),...
    ...на статике хранятся только те, которые нужны для сайта

6. Django Fixtures - json(или xml)-файлы, содержащие структуру БД. В частности, json-это список, в нём несколько словариков,
                                                                                                            ..а в них ключи
    dumpdata - достаёт с БД данные, а loaddata - вносит в БД данные.
    Нужно для перелокации проекта на другие устройства или сохранение версий БД

    Пример:
    python .\manage.py dumpdata products.ProductCategory > categories.json
    т.е dumpdata Приложение.НазваниеМодели > НазваниеФайла Путь(если не указать,
                                                                             то создаст в корневой папке)
    python .\manage.py loaddata products/fixtures/categories.json
    python .\manage.py loaddata products/fixtures/goods.json

7. Для работы с пользователем используется класс User (django.contrib.auth.models). В случае, если необходимо поменять поле..
..создаётся модель User(AbstractUser)
Дальше создаётся форма(forms.py), которой передаётся модель класса(User), уже имеющиеся формы для..
..работы с пользователем(AuthenticationForm, UserCreationForm, UserChangeForm) и forms(from django), там объявляются поля,..
..работу с которыми предстоит произвести. (объявляется тип поля(widget=forms.ТипИнпута(аттрибуты)))
Для изменения данных о пользователе в странице при GET запросе, необходимо отображать данные ПОЛЬЗОВАТЕЛЯ с помощью..
..ИмяForm(instance=request.user), а при добавлении медиа-файла - Form(instance=request.user,..
..data=request.POST, files=request.FILES) в обработке POST-запроса
При успешного заполнения формы пользователя перенаправляют с помощью HttpResponseRedirect(..render, HttpResponseRedirect)..
.. и from django.urls import reverse.
Аутентификация пользователя происходит так: user = auth.authenticate(username=username, password=password) с contrib:auth
Выход пользователя осуществляется при помощи auth.logout(request) и последующем перенаправлением на главную страницу
Сообщения можно выводить через form.non_field_errors и также через contrib:messages.success('message')

8. Миксины - дополнительный функционал для классов. Вставляются перед основным наследуемым классом
    Например: class SomeView(SomeMixin, SomeParentView)
    Используется для объединения общего кода в класс и последующего вызова в отдельных классах

9. Контекстные процессоры - глобальные переменные, которые можно использовать в Templates не передавая их

10. Start server:
    +redis-cli
    +sudo su postgres +psql
    +celery -A store worker -l INFO
    stripe listen --forward-to 127.0.0.1:8000/webhook/stripe/
    and django-server

11. Платёжные системы: Paypal, Stripe, IO

12. Создание нового пользователя на купленном сервере (и последующие шаги деплоя - \
        (https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04)

adduser username
usermod -aG username www-data
(close terminal and login with new user) ssh username@ip

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo -u postgres psql

CREATE DATABASE store_db_production;
CREATE ROLE store_username_production with password 'store_password_production';
ALTER ROLE "store_username_production" WITH LOGIN;
GRANT ALL PRIVILEGES ON DATABASE "store_db_production" to store_username_production;
ALTER USER store_username_production CREATEDB;
\q

sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate

FileZilla - Ctrl+S - NewSite - SFTP(SSH File Transfer Protocol) - ip(buyed VDS-server) > host - user(new) & password >
> connect > mkdir store > перенос файлов(кроме медиа, влючая окружение, флэйки, зависимости) > migrate

static settings > python manage.py collectstatic > runserver 0.0.0.0:8000 (ip:8000 for join to site)


----GUNICORN----
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru#systemd-gunicorn

pip install gunicorn

sudo nano /etc/systemd/system/gunicorn.socket
'''
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
'''

sudo nano /etc/systemd/system/gunicorn.service
'''
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=fdx
Group=www-data
WorkingDirectory=/home/fdx/store-server/store
ExecStart=/home/fdx/store-server/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          store.wsgi:application

[Install]
WantedBy=multi-user.target
'''

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
if error:
    sudo nano /etc/hosts
    '''
    127.0.0.1       localhost store-server (must be)
    '''

sudo systemctl status gunicorn.socket (active)
sudo systemctl status gunicorn

if errors:
    sudo journalctl -u gunicorn (here will be logs)
if update and need to save:
    sudo systemctl daemon-reload
    sudo systemctl restart gunicorn

----nginx----
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru#nginx-gunicorn

sudo apt install nginx
sudo nano /etc/nginx/sites-available/store
'''
server {
    listen 80;
    server_name 77.223.98.200;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/fdx/store-server/store;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
'''
sudo ln -s /etc/nginx/sites-available/store /etc/nginx/sites-enabled
sudo nginx -t (ok)
sudo systemctl restart nginx

----redis----
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-22-04

sudo apt install redis-server
sudo nano /etc/redis/redis.conf
'''
supervised systemd
'''

sudo systemctl restart redis.service
sudo systemctl status redis

TODO:------------------------------------------------APPS & MODULES-----------------------------------------------------
########################################################################################################################
########################################################################################################################
###################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##########################
##################$ THIS WILL BE PLACED APPS AND MODULES, WHICH I USED WITHIN MY PROGGER LIFE $#########################
###################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##########################
########################################################################################################################
########################################################################################################################
------------------------------------------------------------------------------------------------------------------------
TODO:                                                    Email
------------------------------------------------------------------------------------------------------------------------
----in settings.py----------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = '9e7erteagle@gmail.com' - почта, с двухэтапной авторизацией!!!
EMAIL_HOST_PASSWORD = 'kejg krdk rnpo vqcl' - пароль, созданный для приложения
EMAIL_USE_SSL = True
----in models.py-----------------------------------
from django.core.mail import send_mail
send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

------------------------------------------------------------------------------------------------------------------------
TODO:                                                  PostgreSQL
------------------------------------------------------------------------------------------------------------------------
1. Download PostgreSQL from official site - https://www.postgresql.org/download/linux/debian/
----in console-------------------------------------------------------
+sudo su postgres
+psql - these commands also needs for launch server(+\c store_db)

+CREATE DATABASE db_name;
+CREATE ROLE name with password 'password';
+ALTER ROLE "name" WITH LOGIN;
+GRANT ALL PRIVILEGES ON DATABASE "db_name" TO name;
+ALTER USER name CREATEDB;
+ALTER USER username WITH SUPERUSER;

----in Terminal-----------
+sudo apt-get install libpq-dev python3-dev(for first installing, not to venv)
+pip install psycopg2

----in settings.py------------------------------------------------
+DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'store_db',
        'USER': 'store_username',
        'PASSWORD': 'store_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

----in Terminal-----------------------------------------
+python3 manage.py dumpdata appname.Model > name.json
(delete sqlite3.db, makemigrations, migrate)
+python3 manage.py loaddata name.json

------------------------------------------------------------------------------------------------------------------------
TODO:                                                    Redis
------------------------------------------------------------------------------------------------------------------------
1. Download Redis from official site - https://redis.io/docs/install/install-redis/install-redis-on-linux/
----in console----
+redis-cli

----in Terminal--------------
+pip install django-redis

----in settings.py------------------------------------------------
+CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

------------------------------------------------------------------------------------------------------------------------
TODO:                                                    Celery
------------------------------------------------------------------------------------------------------------------------
----in Terminal----------------
+pip install "celery[redis]"

----in store/store/celery.py----------------------------------------
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

app = Celery('store')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

----in store/store/__init__.py--------------------------------------
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)

----in settings.py----------------------------------
# Celery
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'

----in app/tasks.py---------------------------------
from celery import shared_task
...
@shared_task
def function(*args): ...

----in file, where this function will be init-------
from app.tasks import function
...
function.delay(*args)

----in Console or Terminal--------------------------
+celery -A store worker -l INFO

------------------------------------------------------------------------------------------------------------------------
TODO:                                 django-cleanup(cleaning nolink media-files)
------------------------------------------------------------------------------------------------------------------------
----in Terminal--------------
+pip install django-cleanup

----in settings.py------------------------------------------
+INSTALLED_APPS = [
    'django_cleanup.apps.CleanupConfig',
]

------------------------------------------------------------------------------------------------------------------------
TODO:                                flake8(checks the code for compliance with PEP8)
------------------------------------------------------------------------------------------------------------------------
----in Terminal----
+pip install flake8
+flake8 .

----in .flake8----
[flake8]
exclude =
    migrations

ignore =
    F401

max-line-length = 120

------------------------------------------------------------------------------------------------------------------------
TODO:                                            Isort(sorts imports)
------------------------------------------------------------------------------------------------------------------------
----in Terminal----
+pip install isort
+isort .

------------------------------------------------------------------------------------------------------------------------
TODO:                    OAuth(https://django-oauth-toolkit.readthedocs.io/en/latest/install.html)
------------------------------------------------------------------------------------------------------------------------
----in Terminal--------------
+pip install django-allauth

----in settings.py-------------------------------------
+MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
]

+TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.request',
                ...
            ],
        },
    },
]

# OAuth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 3  # ID добавленного сайта(по порядку, первым был example.com, 2й я проебал, 3 щас)

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
        ],
    }
    'someprovider': {}  # https://docs.allauth.org/en/latest/socialaccount/providers/index.html
}

INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',  # some provider app
]

----store/usrl.py--------------------------------
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
]

----in template----------------------------------------------------
{% load socialaccount %}

<a href="{% provider_login_url 'github' %}">
    <i class="fab fa-github fa-2x" style="color: #303030;"></i>
</a>
----------------------------------------------------------------------------------------------
TODO:                                            django-debug-toolbar
------------------------------------------------------------------------------------------------------------------------
----in Terminal----------------------
+pip install django-debug-toolbar

----in settings.py----
INSTALLED_APPS = [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

----in store/urls.py--------------------------------------------------------------
if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # for media-files, not for toolbar

------------------------------------------------------------------------------------------------------------------------
TODO:                   django-humanize(https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/)
------------------------------------------------------------------------------------------------------------------------
----in settings.py--------------
INSTALLED_APPS = [
    'django.contrib.humanize',
]

----in template------
{% load humanize %}

------------------------------------------------------------------------------------------------------------------------
TODO:                                                    Stripe
------------------------------------------------------------------------------------------------------------------------
1. Register on official site - stripe.com
2. Dashboard >> Developers >> API keys >> Publishable key, Secret key
3. Stripe Docs - https://stripe.com/docs >> Get Started >> Online >> Accept online payments

----in settings.py----------------------
# Stripe
STRIPE_PUBLIC_KEY = 'publishable_key'
STRIPE_SECRET_KEY = 'secret_key'

----in Terminal------
pip3 install stripe

----in orders.views------------------------------
import stripe
from http import HTTPStatus

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET_KEY
...
def post(self, request, *args, **kwargs):
    super(OrderCreateView, self).post(request, *args, **kwargs)
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': 'price_1OAAiqCr2nvgUv25VD2k9dQm',  # from Stripe docs
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success')),
        cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_cancelled')),
    )
    return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

------------------------------------------------------------------------------------------------------------------------
TODO:                                 Webhook - How get answer from Striple
------------------------------------------------------------------------------------------------------------------------
1. Fulfillment an end of page >> make as showed(Download Striple CLI, ...) - \
                             https://stripe.com/docs/payments/checkout/fulfill-orders
----in settings.py--------------------------------------------------------------------------------
STRIPE_WEBHOOK_SECRET = 'whsec_edcf5cd984acd15023a1c4771331abf828dde08fc95738e0af9a0e5ae7080f3d'

----in Terminal(after all steps)----------------------------
stripe listen --forward-to 127.0.0.1:8000/webhook/stripe/

----in view---------------------------------------------------------
@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = event['data']['object']

        fulfill_order(session)

    # Passed signature verification
    return HttpResponse(status=200)

def fulfill_order(session):
  # fill me
  print("Fulfilling order")

TODO:-------------------------------------------------------------------------------------------------------------------
TODO:                   THIS DOCUMENTATION MAY BE OLD, NEW INSTRUCTIONS ALWAYS HAVE ON SITE
TODO:-------------------------------------------------------------------------------------------------------------------











































TODO:--------------------------------------------------FIXING BAGS------------------------------------------------------
########################################################################################################################
########################################################################################################################
######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#####################################
#####################################$ THIS WILL BE PLACED BAGS AND THEIR SOLUTION $####################################
######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#####################################
########################################################################################################################
########################################################################################################################
------------------------------------------------------------------------------------------------------------------------
TODO:                                                 Python Console
------------------------------------------------------------------------------------------------------------------------
[ERROR]
django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured.\
                                        You must either define the environment variable DJANGO_SETTINGS_MODULE \
                                        or call settings.configure() before accessing settings.
[FIXING]
1) mark proj(auto-added-dir) as source
2) In Python Console: from proj import wsgi

------------------------------------------------------------------------------------------------------------------------
TODO:                                                    Tests.py
------------------------------------------------------------------------------------------------------------------------
[ERROR]
django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured.\
                                        You must either define the environment variable DJANGO_SETTINGS_MODULE \
                                        or call settings.configure() before accessing settings.
[FIXING]
import os  # for correctly work

import django  # for correctly work

if 'env setting':  # for correctly work
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
    django.setup()









































TODO:--------------------------------------------------SETTINGS.py------------------------------------------------------
########################################################################################################################
########################################################################################################################
######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#####################################
#####################################$ THIS WILL BE PLACED SOME SETTINGS FOR PROJT $####################################
######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#####################################
########################################################################################################################
########################################################################################################################
------------------------------------------------------------------------------------------------------------------------
TODO:                                                    MEDIA
------------------------------------------------------------------------------------------------------------------------
----in settings------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

----in template-----------------------
<form enctype="multipart/form-data">
<img scr="{{ user.image.url }}">

----in store/urls.py------------------------
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [...] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

------------------------------------------------------------------------------------------------------------------------
TODO:                                                    USER
------------------------------------------------------------------------------------------------------------------------
----in settings----------------
AUTH_USER_MODEL = 'users.User'  # if you use a self model of User
LOGIN_URL = '/users/login/ '  # needs for permission decorator
LOGIN_REDIRECT_URL = '/'  # needs for LoginView
LOGOUT_REDIRECT_URL = '/'  # needs for LogoutView

----in views----
from django.contrib.auth.mixins import LoginRequiredMixin

------------------------------------------------------------------------------------------------------------------------
TODO:                                                   STATIC
------------------------------------------------------------------------------------------------------------------------
----in settings-----------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
