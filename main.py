# coding: utf-8

import time


class WeixinMP(object):
    def __init__(self):
        self._access_token_ctime = 0
        self._access_token = None

    @property
    def access_token(self):
        if time.time() - self._access_token_ctime < 7200 and self._access_token:
            return self._access_token
        url = (
            'https://api.weixin.qq.com/cgi-bin/token?'
            'grant_type=client_credential&appid={}&secret={}'
        ).format(self.appid, self.secret)

