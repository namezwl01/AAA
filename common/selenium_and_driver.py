#coding = utf-8
from selenium import webdriver
import logging
from logging import config
File_config = "../config/log.conf"
config.fileConfig(File_config)
logger = logging.getLogger()
from selenium.webdriver.chrome.options import Options
import os
import sys
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

def selenium_And_Driver():
    opt = Options()
    # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    # opt.set_headless()
    # CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
    # GOOGLE_CHROME_SHIM = os.getenv('GOOGLE_CHROME_SHIM', "chromedriver")
    opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-dev-shm-usage')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # opt.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
if __name__ == '__main__':
    selenium_And_Driver()
    logger.info("webdriver初始化完成")

