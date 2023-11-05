from django.contrib import admin

# Register your models here.
# Регистрация, созданной в данном приложении, таблицы=модели для отображения её в Админ-панели
from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # Отображение объектов
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')  # Отображение объекта
    # readonly_fields = ('description',)
    search_fields = ('name',)  # Поиск по имени
    ordering = ('name',)  # Сортировка по алфавитному порядку -name для обратному отображению


class BasketAdmin(admin.TabularInline):  # Для Foreign связи
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0  # default = 3, доп поля
