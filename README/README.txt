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

8. Как пофиксить Python Console:
a) Пометить проект, который был создан командой django-admin startproject *название проекта*, как sourse root
b) импортировать: from store import wsgi, где store - каталог(приложение), созданный автоматически, с таким же названием..
   ..как и проект

9. Пагинация: https://docs.djangoproject.com/en/4.2/topics/pagination/#top

10. Сравнение FBV(Function-based views) и CBV(Class-based views), картинка в файле FBV_CBV.png
https://docs.djangoproject.com/en/4.2/ref/class-based-views/

11. Миксины - дополнительный функционал для классов. Вставляются перед основным наследуемым классом
    Например: class SomeView(SomeMixin, SomeParentView)
    Используется для объединения общего кода в класс и последующего вызова в отдельных классах

12. Media:
in template: +<form enctype="multipart/form-data"> + <img scr="{%if..., {{ user.image.url }} ..else..default..endif%}">

in main urls:
+from django.conf import settings
+from django.conf.urls.static import static
+urlpatterns = [...] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

in settings: +MEDIA_URL = '/media/' +MEDIA_ROOT = BASE_DIR / 'media'

12.2 clean nolinked media-files
+pip install django-cleanup
+INSTALLED_APPS = ( ..., 'django_cleanup.apps.CleanupConfig',)

13. Users settings
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/users/login/ '
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

14. Email
EMAIL_BACKEND = 'django.core.mail.backend.console.EmailBackend'