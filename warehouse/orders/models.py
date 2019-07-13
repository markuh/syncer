from django.db import models

from . import STATUSES_LIST, STATUS_NEW
from .utils import StoreApi


class Order(models.Model):
    """
    Orders model
    """
    order_id = models.IntegerField(unique=True)
    product = models.IntegerField("Product ID")
    count = models.IntegerField()
    status = models.SmallIntegerField(choices=STATUSES_LIST, default=STATUS_NEW)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Send order changes to Store
        """
        no_sync = kwargs.pop("no_sync", False)
        super().save(*args, **kwargs)

        if no_sync:
            # skip trigger on external update
            return

        StoreApi.update_order(self)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        """
        """
        return "{} {} {}".format(self.order_id, self.product, self.count)

    def serialize(self):
        """
        Serialize model for API request
        """
        return {
            "status": self.status,
        }
