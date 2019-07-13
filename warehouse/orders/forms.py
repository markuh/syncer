from django import forms

from .models import Order


class CreateOrderApiForm(forms.ModelForm):
    """
    Create new order API request validation form
    """
    class Meta:
        model = Order
        fields = ["order_id", "product", "count", 'status']


class UpdateOrderApiForm(forms.ModelForm):
    """
    Update order API request validation form
    """
    class Meta:
        model = Order
        fields = ['status', "count"]
