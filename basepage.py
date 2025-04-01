# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 14:44
# @Author  : mmy
# @File    : basepage.py

import time
import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from common import mylog
from common import constant
from pagelocators.page_locator import BaseLoc, Locator


class BasePage:

    def __init__(self, dirver: webdriver.Chrome):
        self.driver = dirver
        self.log = mylog.log()
        self.l = Locator()
        self.baseLoc = BaseLoc(self.driver)

    def max_window(self):
        return self.driver.maximize_window()

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def save_screen(self, filename):
        file_path = os.path.join(constant.screenshots_dir, "{}_{}.jpg".format(filename, time.time()))
        self.driver.save_screenshot(file_path)
        return file_path

    def move_to_ele(self,ele):
        action=ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
