from django import forms
from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    """
    """
    can_delete = False
    list_display = ("order_id", 'product', 'count', "status", "created_at")
    readonly_fields = ("order_id", "product", "count", "created_at")
    date_hierarchy = "created_at"
    search_fields = ("customer_info", )

    def has_add_permission(self, request):
        """
        Cant create order in warehouse
        """
        return False


admin.site.register(Order, OrderAdmin)
