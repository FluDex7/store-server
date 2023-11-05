from http import HTTPStatus

#  Решение проблемы запуска тестов
import os
import django

if 'env setting':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
    django.setup()

from django.test import TestCase
from django.urls import reverse

from products.models import Product


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertEqual(response.context_data['view'].template_name, 'products/index.html')
        # self.assertTemplateUsed(response, 'products/index.html') вместо этого


class ProductsListViewTestCase(TestCase):
    fixtures = ['Categories.json', 'Products.json']

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        products = Product.objects.all()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertEqual(response.context_data['view'].template_name, 'products/products.html')
        self.assertEqual(response.context_data['object_list'], products)
