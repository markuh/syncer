from django.urls import path

from .views import CreateOrderView, UpdateOrderView, DeleteOrderView

app_name = "orders"


urlpatterns = [
    path('create', CreateOrderView.as_view(), name='create_order'),
    path('<int:order_id>/update', UpdateOrderView.as_view(), name='update_order'),
    path('<int:order_id>/delete', DeleteOrderView.as_view(), name='delete_order'),
]
