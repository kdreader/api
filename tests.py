# encoding: utf8

import pytest
import requests_mock
from django.conf import settings

from sms import SMS

PHONE = '18600363396'
CAPTCHA = '1234'


class TestSMS(object):
    @pytest.fixture(scope='class')
    def sms(self):
        return SMS(settings.SMS['HOST'], settings.SMS['PRODUCT'])

    def test_register(self, sms):
        with requests_mock.mock() as m:
            url = sms.host + '/v1/api/sms/register/'
            m.post(url, text='')
            assert sms.register(PHONE) is True

    def test_login(self, sms):
        with requests_mock.mock() as m:
            url = sms.host + '/v1/api/sms/login/'
            m.post(url, text='')
            assert sms.login(PHONE) is True

    def test_verify_code(self, sms):
        with requests_mock.mock() as m:
            url = sms.host + '/v1/api/sms/verify_code/'
            m.post(url, text='')
            assert sms.verify_code(PHONE) is True

    def test_verify(self, sms):
        with requests_mock.mock() as m:
            url = sms.host + '/v2/api/sms/verify/'
            m.get(url, text='{"valid": true}')
            assert sms.verify(PHONE, CAPTCHA) in (True, False,)
