# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 10:56
# @Author  : mmy
# @File    : main.py

import pytest

if __name__ == '__main__':
    pytest.main(['--env=test', '--capture=no', '--alluredir=outputs/results'])
