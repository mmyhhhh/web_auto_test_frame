# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 16:53
# @Author  : mmy
# @File    : page_locator.py

import os
import time
from typing import Dict, Optional, Tuple, Any

import yaml
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import constant
from common import mylog


class PageLoc:

    def __init__(self, pagename: Dict):
        for k, v in pagename.items():
            self.__setattr__(k, v)


class Locator:
    def __init__(self):
        with open(constant.locator_path, mode='r+', encoding='utf-8') as f:
            locators_dic = yaml.safe_load(f)
            self.locator_map = {}
            for page in locators_dic["pages"]:
                page_name = page["page"]["pagename"]

                self.locator_map[page_name] = {}
                locator_list = page['page']['locator']
                for locator in locator_list:
                    name = locator['name']
                    by_type = locator['type']
                    value = locator['value']
                    self.locator_map[page_name][name] = {'by_type': by_type, 'value': value}

        for k, v in self.locator_map.items():
            self.__setattr__(k, PageLoc(v))


class BaseLoc:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.log = mylog.log()

    def get_locator(self, ele_loc):
        by_type = ele_loc["by_type"]
        value = ele_loc["value"]
        if by_type == "xpath":
            return (By.XPATH, value)
        elif by_type == "id":
            return (By.ID, value)
        elif by_type == "class":
            return (By.CLASS_NAME, value)
        elif by_type == "tag":
            return (By.TAG_NAME, value)
        elif by_type == "name":
            return (By.NAME, value)
        elif by_type == "link text":
            return (By.LINK_TEXT, value)
        elif by_type == "partial link text":
            return (By.PARTIAL_LINK_TEXT, value)
        else:
            return

    def get_visible_element(self, ele_loc, eqc=60):
        locator = self.get_locator(ele_loc)
        try:
            WebDriverWait(self.driver, eqc).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(locator[0], locator[1])
        except Exception as e:
            self.log.error("not find element:" + locator[-1])
            self.driver.save_screenshot(os.path.join(constant.screenshots_dir, "screen_{}.jpg".format(time.time())))

    def text_to_be_present_in_element(self, ele_loc, text, eqc=60):
        locator = self.get_locator(ele_loc)
        try:
            WebDriverWait(self.driver, eqc).until(EC.text_to_be_present_in_element(locator, text))
            return self.driver.find_element(locator[0], locator[1])
        except Exception as e:
            self.log.error(e)
            self.driver.save_screenshot(os.path.join(constant.screenshots_dir, "screen_{}.jpg".format(time.time())))

    def el_list(self, index, ele_loc):
        by_type = ele_loc["by_type"]
        value = ele_loc["value"]
        value = value.format(index)
        return self.get_visible_element({"by_type": by_type, "value": value})
