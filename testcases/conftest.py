# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 15:34
# @Author  : mmy
# @File    : conftest.py.py

import os
import time
import json
import pytest
import httprunner
from selenium import webdriver

from common import constant
from common import mylog
from common.do_config import ReadConfig

log = mylog.log()
do_config = ReadConfig()
env_data = "test"
global_data = {}


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="test", help="Set the environment (test, product)"
    )


@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--env")  # 获取命令行传入的--env参数或默认值


# 通过pytest命令参数 --env="test" or --env="product" 来切换测试服或者正式服环境
@pytest.fixture(scope="session")
def init_driver(environment):
    url = do_config.get_env("web_address", "test_address")
    set_api_env("test")
    if environment == "product":
        url = do_config.get_env("web_address", "product_address")
        set_api_env("product")
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    yield driver
    time.sleep(3)
    driver.quit()


# 为了web端测试过程中获取到的参数值传入接口用例中使用，所以设置了conftest的全局变量
@pytest.fixture()
def set_global_data():
    def _set_global_data(key, value):
        global_data[key] = value

    return _set_global_data


@pytest.fixture()
def get_global_data():
    def _get_global_data(key):
        return global_data.get(key)

    return _get_global_data


# 自动切换接口用例的环境，获取当前pytes命令中env的参数值，根据参数值将配置文件中的test_env或者product_env写入httprunner中的.env文件中
def set_api_env(env):
    with open(constant.hp_api_env, mode="w", encoding="utf-8") as f:
        vars = do_config.get_options("test_env")
        for var in vars:
            value = do_config.get_env("test_env", var)
            f.write(var + "=" + value)
            f.write("\n")

        if env == "product":
            vars = do_config.get_options("product_env")
            for var in vars:
                value = do_config.get_env("product_env", var)
                f.write(var + "=" + value)
                f.write("\n")


# 执行接口用例，获取后端配置数据用于与前端显示数据做校验
def run_api(file_path):
    log.info("执行接口用例")
    hr = httprunner.HttpRunner()
    try:
        hr.run_path(file_path)
        summary = hr.get_summary()
        return summary
    except:
        log.error("接口用例执行失败")


# 执行httprunner获取配置数据
@pytest.fixture()
def get_op_configure(set_global_data):
    try:
        summary = run_api(constant.hp_get_layout)
        # 获取接口用例执行后extract出的数据，yml文件中需要使用export 将提取的参数声明输出
        configure_switch = summary.in_out.export_vars["configure_switch"]
        config_list = []
        pack_kind = "123"
        pack_id = "123"
        # 将变量设置为全局变量供接口用例调用
        set_global_data("cube_id", pack_id)
        cube_summary = run_api(constant.hp_get_cube)
        cube = cube_summary.in_out.export_vars["cube"]
        config_list.append({pack_kind: cube})
        yield configure_switch, config_list
    except:
        log.error("接口用例执行失败")
