import os  # для правильного запуска тестов
from http import HTTPStatus

import django  # для правильного запуска тестов
from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory

if 'env setting':  # для правильного запуска тестов
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
    django.setup()


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

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_test(response)
        self.assertEqual(list(response.context_data['object_list']), list(self.products[:3]))

    def test_list_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_test(response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=category.id))
        )

    def _common_test(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertEqual(response.context_data['view'].template_name, 'products/products.html')
