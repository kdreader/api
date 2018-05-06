# encoding: utf-8

import json
import urllib
import requests

__all__ = ('SMS',)


def compose_url(host, path, query_string=None):
    url = host + path
    if query_string:
        assert isinstance(query_string, dict)
        url += '?' + urllib.urlencode((query_string))
    return url


class SMS(object):
    def __init__(self, host, product):
        self._host = host
        self._product = product

    @property
    def product(self):
        return self._product

    @property
    def host(self):
        return self._host

    def register(self, phone):
        path = '/v1/api/sms/register/'
        data = {
            'product': self.product,
            'phone': phone,
        }
        url = compose_url(self.host, path,)
        resp = requests.post(url, json=data)
        if resp.status_code == 200:
            return True
        else:
            return False

    def login(self, phone):
        path = '/v1/api/sms/login/'
        data = {
            'product': self.product,
            'phone': phone,
        }
        url = compose_url(self.host, path,)
        resp = requests.post(url, json=data)
        if resp.status_code == 200:
            return True
        else:
            return False

    def verify_code(self, phone):
        path = '/v1/api/sms/verify_code/'
        data = {
            'product': self.product,
            'phone': phone,
        }
        url = compose_url(self.host, path,)
        resp = requests.post(url, json=data)
        if resp.status_code == 200:
            return True
        else:
            return False

    def verify(self, phone, captcha):
        path = '/v2/api/sms/register/'
        data = {
            'phone': phone,
            'captcha': captcha,
        }
        url = compose_url(self.host, path)
        resp = requests.get(url, data)
        if resp.status_code == 200 and json.loads(resp.content)['valid'] is True:
            return True
        else:
            return False
