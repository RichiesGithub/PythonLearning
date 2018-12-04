#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import datetime

# chromedriver = "/usr/bin/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome()
def login(uname, pwd):
    driver.get("https://www.taobao.com")
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
    input(uname, pwd)

    # 点击购物车里全选按钮
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    # time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def input(uname, pwd):
    time.sleep(3)
    # # 选择密码登录
    # if driver.find_element_by_id("J_Quick2Static"):
    #     driver.find_element_by_id("J_Quick2Static").click()
    # time.sleep(3)

    # # 用户名输入
    # if driver.find_element_by_name("TPL_username"):
    #     for i in uname:
    #         driver.find_element_by_name("TPL_username").send_keys(i)
    #         time.sleep(0.5)
    # time.sleep(3)
    #
    # # 密码输入
    # if driver.find_element_by_name("TPL_password"):
    #     for j in pwd:
    #         driver.find_element_by_name("TPL_password").send_keys(j)
    #         time.sleep(0.5)
    # time.sleep(3)
    if driver.find_element_by_class_name('alipay-login'):
        driver.find_element_by_class_name('alipay-login').click()
    if driver.find_element_by_id('J_Static2Quick'):
        driver.find_element_by_id('J_Static2Quick').click()

    time.sleep(5)
# 点击登录按钮
    if driver.find_element_by_id("J_SubmitStatic"):
        driver.find_element_by_id("J_SubmitStatic").click()
    time.sleep(3)
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(2)


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if now == buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                driver.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(1)
        print(now)
        time.sleep(1)


if __name__ == "__main__":
    # 中文账号记得decode编码
    login("13608311930", 'lq910816')
    buy('2018-01-30 13:35:00')
