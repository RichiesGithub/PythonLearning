#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

from selenium import webdriver
import time
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf8')
driver = webdriver.Chrome()
def login():
    driver.get("https://www.taobao.com")
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
    Input()

    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    # time.sleep(3)
    now = datetime.datetime.now()
    print now
    Buy('2018-11-11 00:00:00')
    print '执行了buy'
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def Input():
    time.sleep(3)
    if driver.find_element_by_class_name('alipay-login'):
        driver.find_element_by_class_name('alipay-login').click()
    time.sleep(5)
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

def Buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if now == buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                search_windows = driver.current_window_handle
                # if driver.find_element_by_class_name('go-btn'):
                #     driver.find_element_by_class_name('go-btn').click()

                if driver.find_element_by_link_text('提交订单'):
                    driver.find_element_by_link_text('提交订单').click()
                    print '11111'
            except Exception,e:
                time.sleep(1)
                print e
        print(now)
        time.sleep(1)

if __name__ == "__main__":
    # 中文账号记得decode编码
    login()
