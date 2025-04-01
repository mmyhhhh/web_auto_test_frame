# -*- coding: utf-8 -*-
# @Time    : 2025/3/17 13:44
# @Author  : mmy
# @File    : constant.py

import os

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env_config=os.path.join(os.path.join(base_dir,"config"),"env.config")
outputs_dir=os.path.join(base_dir,"outputs")
log_path=os.path.join(os.path.join(outputs_dir,"logs"),"log.log")
screenshots_dir=os.path.join(outputs_dir,"screenshots")
locator_path=os.path.join(os.path.join(base_dir,"pagelocators"),"page_locators.yml")

# 接口yml用例文件路径
hp_case_dir = os.path.join(os.path.join(base_dir, 'api_run'), 'testcases')
hp_api_env=os.path.join(os.path.join(base_dir, 'api_run'),".env")
hp_get_layout=os.path.join(hp_case_dir,"get_config_switch.yml")
hp_get_layout_pc_sale=os.path.join(hp_case_dir,"get_layout_pc_sale.yml")
hp_get_layout_mall=os.path.join(hp_case_dir,"get_layout_malllayout.yml")
hp_get_cube=os.path.join(hp_case_dir,"get_cube.yml")
