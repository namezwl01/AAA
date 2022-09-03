#coding = utf-8
import os
import sys
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

import csv

import time
from selenium.webdriver.common.by import By

from common.selenium_and_driver import selenium_And_Driver


class PageOBject(object):
    def __init__(self,Driver):
        self.driver = Driver

    def find_Element(self,*args):
        return  self.driver.find_element(*args)
    #这是找单个元素的方法

    def find_Elements(self,*args):
        return  self.driver.find_elements(*args)
        # 这是找多个元素的方法

    def only_Element(self,my_text,*args):
        element_List = self.find_Elements(*args)
        for  element in element_List:
            if element.text == my_text:
                return element.click()
    # 这是从多个元素中找到自己想要元素的方法

    def subscript_Element(self,subscript,*args):
        element_List = self.find_Elements(*args)
        return element_List[subscript].click()
    # 这是从多个元素中找到自己
    # 这是从多个元素中找到自己所传下标的元素并点击


        # csv文件的读取


    def getCsvDataByLine(self, csv_file, line):
        file = open(file=csv_file, mode='r', encoding='gbk')
        # 把表格里面所有的数据读取,记录到reader对象
        reader = csv.reader(file)
        for index, row in enumerate(reader, 1):
            # 判断行号是否和当前索引一样，如果一样，直接返回数据index，从1开始
            if index == line:
                file.close()
                return row
    def time_sleep(self,t):
        time.sleep(t)



    def get_Png(self):
        return self.driver.get_screenshot_as_png()

    def executE_Script(self,*args):
        e = self.driver.find_element(*args)  # 找到下一屏幕唯一的一个元素 ，
        self.driver.execute_script("arguments[0].scrollIntoView();", e)






