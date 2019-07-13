from django.urls import path

from .views import UpdateOrderView

app_name = "orders"


urlpatterns = [
    path('<int:order_id>/update', UpdateOrderView.as_view(), name='update_order'),
]
