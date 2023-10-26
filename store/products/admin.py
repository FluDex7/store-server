from django.contrib import admin

# Register your models here.
# Регистрация, созданной в данном приложении, таблицы=модели для отображения её в Админ-панели
from products.models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)
