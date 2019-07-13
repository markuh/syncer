from django.views.generic import View
from django.http import JsonResponse

from .forms import CreateOrderApiForm, UpdateOrderApiForm
from .models import Order


class CreateOrderView(View):
    """
    API view for receive new order info from store
    """
    def post(self, request, *args, **kwargs):
        """
        """
        form = CreateOrderApiForm(request.POST)
        if not form.is_valid():
            return JsonResponse({"status": False, "error": {"validation": form.errors}})

        order = form.save(commit=False)
        order.save(no_sync=True)

        return JsonResponse({"status": True, "data": {"order_id": order.id}})


class UpdateOrderView(View):
    """
    API view for update order info from store
    """
    def post(self, request, order_id, *args, **kwargs):
        """
        """
        try:
            order = Order.objects.get(order_id=int(order_id))
        except (ValueError, TypeError):
            return JsonResponse({"status": False, "error": "Unexpected order id"})
        except Order.DoesNotExist:
            return JsonResponse({"status": False, "error": "Order not found"})

        form = UpdateOrderApiForm(request.POST, instance=order)
        if not form.is_valid():
            return JsonResponse({"status": False, "error": {"validation": form.errors}})
        instance = form.save(commit=False)
        instance.save(no_sync=True)

        result = {
            "status": True,
            "data": {
                "order_status": order.status,
            }
        }
        return JsonResponse(result)


class DeleteOrderView(View):
    """
    API view for delete order
    """
    def delete(self, request, order_id, *args, **kwargs):
        """
        """
        try:
            order = Order.objects.get(order_id=int(order_id))
        except (ValueError, TypeError):
            return JsonResponse({"status": False, "error": "Unexpected order id"})
        except Order.DoesNotExist:
            return JsonResponse({"status": False, "error": "Order not found"})

        order.delete()
        return JsonResponse({"status": True})
