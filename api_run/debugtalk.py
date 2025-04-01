# -*- coding: utf-8 -*-
# @Time    : 2025/3/18 17:24
# @Author  : mmy
# @File    : debugtalk.py

import time
import datetime
import json

from httprunner import __version__
from common.mylog import log
from common.request_utils import Request
from testcases import conftest


class PostParams:
    pass


def get_httprunner_version():
    return __version__


def get_file(file_path):
    return open(file_path, mode='rb')


def get_host(base_url):
    return base_url[8:]

def get_cube_id():
    data=conftest.global_data
    cube_id=data.get("cube_id")
    return str(cube_id)

