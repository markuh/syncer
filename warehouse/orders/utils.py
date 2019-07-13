import requests

from django.conf import settings


class StoreApi:
    """
    Simple API client for Store
    """
    @staticmethod
    def update_order(order):
        """
        Update order call
        """
        return StoreApi._req("{}/update".format(order.id), "post", order.serialize())

    @staticmethod
    def _req(method_url, method, data=None):
        """
        Send request to remote API
        """
        req_method = getattr(requests, method)
        if req_method is None:
            return None

        url = "/".join([settings.STORE_URL, method_url])
        r = req_method(url, data)
        return r.json()
