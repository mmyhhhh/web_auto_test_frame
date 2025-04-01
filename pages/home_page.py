# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 16:26
# @Author  : mmy
# @File    : home_page.py

from selenium.webdriver import Chrome
from basepage import BasePage


class HomePage(BasePage):

    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self.baseLoc.get_visible_element(self.l.navigation.home_page_tab).click()

    def get_login_button(self):
        # self.l.home_page.login_button其中home_page为page名称，login_button为元素名称，可以获取该元素的定位方式和定位值
        return self.baseLoc.get_visible_element(self.l.home_page.login_button)

    def get_login_username(self):
        return self.baseLoc.get_visible_element(self.l.home_page.login_username)

    def get_login_pwd(self):
        return self.baseLoc.get_visible_element(self.l.home_page.login_pwd)

    def get_login_submit(self):
        return self.baseLoc.get_visible_element(self.l.home_page.login_submit)

    def login(self, phone, password):
        button = self.get_login_button()
        button.click()
        username = self.get_login_username()
        username.send_keys(phone)
        pwd = self.get_login_pwd()
        pwd.send_keys(password)
        submit = self.get_login_submit()
        submit.click()
