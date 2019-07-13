from django import forms

from .models import Order


class OrderApiForm(forms.ModelForm):
    """
    Order API request data validation form
    """
    class Meta:
        model = Order
        fields = ['status']
