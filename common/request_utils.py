# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 14:10
# @Author  : mmy
# @File    : request_utils.py

import requests


class Request:

    def __init__(self):
        self.session = requests.sessions.Session()

    def __enter__(self):
        # print('开启会话:', self)
        # print('开启会话:', self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('执行完毕准备关闭会话:', self)
        # print('执行完毕准备关闭会话:', self.session)
        self.close()
        # print('关闭会话:', self)
        # print('关闭会话:', self.session)
        res = self.session.cookies
        print(res)

    def __new__(cls, *args, **kwargs):
        # print('创建实例')
        return super().__new__(cls)

    def request(self, method, url, **kwargs):
        method = method.upper()
        return self.session.request(method=method, url=url, **kwargs)

    def close(self):
        self.session.close()