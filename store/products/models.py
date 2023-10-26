from django.db import models

# Create your models here.
# здесь будет создаватся таблица для БД
# Модели = таблицы

class ProductCategory(models):
    # поле = тип
    name = models.CharField(max_length=128, unique=True)  # max_length - обязательный атрибут для типа CharField
    description = models.TextField(null=True, blank=True)