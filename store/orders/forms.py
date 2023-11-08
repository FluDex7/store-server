from django import forms

from orders.models import Order


class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')