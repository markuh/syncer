from django import forms
from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    """
    """
    save_on_top = True
    list_display = ("pk", 'product', 'count', "price", "status", "customer_info", "created_at")
    date_hierarchy = "created_at"
    search_fields = ("customer_info", )


admin.site.register(Order, OrderAdmin)
