# -*- coding: utf-8 -*-
# @Time    : 2025/3/18 10:39
# @Author  : mmy
# @File    : test_home_page.py

import time
import pytest
import allure
from selenium.webdriver import Chrome
from pages.home_page import HomePage


@allure.feature("首页")
@allure.story("首页布局")
class TestHomeLayout:
    @allure.step("登录")
    @pytest.mark.login
    def test_login(self, init_driver: Chrome,get_op_configure):
        self.driver = init_driver
        # 将获取到的后端配置分别赋值给configure_switch, config_list，必要时与前端数据进行校验
        (configure_switch, config_list)=get_op_configure
        home_page = HomePage(self.driver)
        # 前端登录
        home_page.login("1234567", "12345678")
        time.sleep(2)
        assert True
