# encoding: utf8

import json
import requests


class GeoIp(object):
    """
    Get geo information by IP.
    """
    default_timeout = 3

    def get_geo(self, ip, **kwargs):
        raise NotImplementedError()


class TaobaoGeoIp(GeoIp):
    """
    Get geo information by IP.

    GEO information:
    ```json
    {
        "country": "中国",
        "country_id": "CN",
        "area": "华东",
        "area_id": "300000",
        "region": "福建省",
        "region_id": "350000",
        "city": "厦门市",
        "city_id": "350200",
        "county": "",
        "county_id": "-1",
        "isp": "电信",
        "isp_id": "100017",
        "ip": "110.84.0.129"
    }
    ```
    """
    default_service_url_pattern = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s'

    def get_geo(self, ip, **kwargs):
        url = self.default_service_url_pattern % ip
        timeout = kwargs.get('timeout', self.default_timeout)
        response = requests.get(url, timeout)
        return json.loads(response.content)['data']
