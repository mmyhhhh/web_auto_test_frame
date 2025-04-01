# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 13:48
# @Author  : mmy
# @File    : do_config.py

import configparser

from common import constant


class ReadConfig:

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(constant.env_config,encoding="utf-8")

    def get_env(self,section,option):
        return self.config.get(section,option)

    def get_log_level(self):
        return self.config.get('log', 'level')

    def get_options(self,section):
        return self.config.options(section)
