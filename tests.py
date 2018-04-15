# encoding: utf8

import pytest
from django.conf import settings

from sms import SMS

PHONE = '18600363396'
CAPTCHA = '1234'


class TestSMS(object):
    @pytest.fixture(scope='class')
    def sms(self):
        return SMS(settings.SMS['HOST'], settings.SMS['PRODUCT'])

    def test_register(self, sms):
        assert sms.register(PHONE) is True

    def test_verify(self, sms):
        assert sms.verify(PHONE, CAPTCHA) in (True, False,)
