from django.db import models

# Create your models here.
# здесь будет создаватся таблица для БД
# Модели = таблицы
from users.models import User

class ProductCategory(models.Model):
    # поле = тип
    name = models.CharField(max_length=128, unique=True)  # max_length - обязательный атрибут для типа CharField
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
        # Каскадное удаление - удаление всех связанных данных с данной категорией
        # models.PROTECT - запретит удалять данные, пока у данной категории есть товары
        # models.SET_DEFAULT - ставит значение по умолчанию, если категорию удалить

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)  # Автоматически заполняется

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'