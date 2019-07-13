from django.views.generic import View
from django.http import JsonResponse

from .forms import OrderApiForm
from .models import Order


class UpdateOrderView(View):
    """
    Update order API view
    """

    def post(self, request, order_id, *args, **kwargs):
        """
        """
        try:
            order = Order.objects.get(pk=int(order_id))
        except (ValueError, TypeError):
            return JsonResponse({"status": False, "error": "Unexpected order id"})
        except Order.DoesNotExist:
            return JsonResponse({"status": False, "error": "Order not found"})

        form = OrderApiForm(request.POST, instance=order)
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
