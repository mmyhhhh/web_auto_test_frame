# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 14:02
# @Author  : mmy
# @File    : mylog.py

import logging
from logging.handlers import RotatingFileHandler

from common.do_config import ReadConfig
from common import constant

log_file = constant.log_path


def log():
    # 日志输出等级（从配置文件中读取）
    ccf = ReadConfig()
    setlevel = ccf.get_log_level()
    # 设置日志收集器
    logger = logging.getLogger('log')
    # 设置收集器收集等级
    logger.setLevel('DEBUG')
    # RotatingFileHandler(constant.log_file,maxBytes=20*1024*1024,backupCount=2,encoding='utf-8')
    # 设置日志输出渠道
    handlers=logger.handlers
    if handlers:
        handler=handlers[0]
    else:
        handler = RotatingFileHandler(log_file, maxBytes=20 * 1024 * 1024, backupCount=2, encoding='utf-8')
        # 设置日志输出等级
        handler.setLevel(setlevel)
    # 设置日志输出格式
    formatter = logging.Formatter("%(asctime)s-[%(levelname)s]-%(filename)s-%(module)s-%(lineno)d-%(message)s")
    handler.setFormatter(formatter)
    # 日志输出器与收集器匹配
    logger.addHandler(handler)

    return logger
