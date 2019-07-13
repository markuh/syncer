import requests

from django.conf import settings


class WarehouseApi:
    """
    Simple API client for Warehouse
    """
    @staticmethod
    def create_order(order):
        """
        Create new order call
        """
        return WarehouseApi._req("create", "post", order.serialize())

    @staticmethod
    def update_order(order):
        """
        Update order call
        """
        return WarehouseApi._req("{}/update".format(order.id), "post", order.serialize())

    @staticmethod
    def delete_order(order):
        """
        Delete order call
        """
        return WarehouseApi._req("{}/delete".format(order.id), "delete")

    @staticmethod
    def _req(method_url, method, data=None):
        """
        Send request to remote API
        """
        req_method = getattr(requests, method)
        if req_method is None:
            return None

        url = "/".join([settings.WAREHOUSE_URL, method_url])
        request_args = [url]
        if data is not None:
            request_args.append(data)

        r = req_method(*request_args)
        return r.json()
