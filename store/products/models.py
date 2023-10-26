from django.db import models

# Create your models here.
# здесь будет создаватся таблица для БД
# Модели = таблицы


class ProductCategory(models.Model):
    # поле = тип
    name = models.CharField(max_length=128, unique=True)  # max_length - обязательный атрибут для типа CharField
    description = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    # Каскадное удаление - удаление всех связанных данных с данной категорией
    # models.PROTECT - запретит удалять данные, пока у данной категории есть товары
    # models.SET_DEFAULT - ставит значение по умолчанию, если категорию удалить
