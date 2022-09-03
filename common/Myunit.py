#coding = utf-8
import unittest
import os
import sys
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from common.selenium_and_driver import logger, selenium_And_Driver

class MyUnit(unittest.TestCase):

    def setUp(self):
        logger.info("_______获取驱动________")
        self.driver = selenium_And_Driver()

    def tearDown(self):
        logger.info("_______测试完毕，驱动关闭________")
        self.driver.quit()
        os.system("pkill chrome")
        os.system("pkill chromedriver")
#a
if __name__ == '__main__':
    MyUnit.main()
    