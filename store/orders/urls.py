from django.urls import path

from orders.views import (CanceledTemplateView, OrderCreateView,
                          SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order_success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order_cancelled/', CanceledTemplateView.as_view(), name='order_cancelled'),
]
