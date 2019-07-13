from django.db import models
from django.db.models.signals import post_delete

from . import STATUSES_LIST, STATUS_NEW
from .utils import WarehouseApi


class Order(models.Model):
    """
    Orders model
    """
    product = models.IntegerField("Product ID")
    count = models.IntegerField()
    price = models.FloatField()
    customer_info = models.TextField()
    status = models.SmallIntegerField(choices=STATUSES_LIST, default=STATUS_NEW)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Send order changes to Warehouse
        """
        is_new = self.pk is None
        no_sync = kwargs.pop("no_sync", False)

        super().save(*args, **kwargs)

        if no_sync:
            # skip sync for incoming changes
            return

        if is_new:
            WarehouseApi.create_order(self)
        else:
            WarehouseApi.update_order(self)

    @staticmethod
    def delete_instance(instance, **kwargs):
        """
        Send order deletion to Warehouse
        """
        WarehouseApi.delete_order(instance)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        """
        """
        return "{} {} {}".format(self.product, self.count, self.price)

    def serialize(self):
        """
        Serialize model for API request
        """
        return {
            "order_id": self.id,
            "product": self.product,
            "count": self.count,
            "status": self.status,
        }


post_delete.connect(Order.delete_instance, sender=Order)
