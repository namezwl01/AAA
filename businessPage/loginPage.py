#coding = utf-8
from selenium.webdriver.common.by import By

from PageObject.pageObject import PageOBject
from common.selenium_and_driver import logger
from data.BaseUrl import login_url


class LoginPage(PageOBject):
    usernameInput = (By.CSS_SELECTOR,'input[placeholder="151xxxxx789/example@didiyun.com"]')
    passwordInput = (By.CSS_SELECTOR,'input[placeholder="8~16位，包含大小写字母、数字、特殊字符"]')
    button = (By.CSS_SELECTOR,'button[class="el-button option-buttom-full success-btn el-button--primary"][type="submit"]')
    check_button = (By.CSS_SELECTOR,'button[class="el-button charge el-button--primary el-button--small"]')

    def Login_business(self,username,password):
        self.driver.get(login_url)
        logger.info("_________打开首页__________")
        self.find_Element(*self.usernameInput).send_keys(username)
        logger.info("_________输入用户名__________")
        self.find_Element(*self.passwordInput).send_keys(password)
        logger.info("_________输入密码__________")
        self.find_Element(*self.button).click()
        self.time_sleep(6)

    def check_login(self):
        try:
            a = self.find_Element(*self.check_button)
            print(a)
            if a != None:
                logger.info("_________登录成功了__________")
                return True
            else:
                    if a == None:
                        return False
        except Exception as E:
            print(E)




