#coding = utf-8

from PageObject.pageObject import PageOBject
from common.selenium_and_driver import logger
from data.BaseUrl import create_ESB
from selenium.webdriver.common.by import By

class Create_EBS_C(PageOBject):
    a = (By.CSS_SELECTOR, 'button[class="el-button el-button--default el-button--primary "]')
    create_EBS_button = (By.CSS_SELECTOR,'button[class="el-button create-newebs-btn el-button--primary el-button--large"]')#创建云盘的按钮
    EBS_type = (By.CSS_SELECTOR,'div[class="custom-label"]') #EBS类型选择
    pay = (By.CSS_SELECTOR,'p[class="mid"]')#规格选择项
    i = (By.CSS_SELECTOR,'div[class="form-item-label"]')
    pay_type = (By.CSS_SELECTOR,'span[class="el-radio-button__inner"]') #付费方式选择项
    EBs_name = (By.CSS_SELECTOR, 'input[placeholder="填写云盘名称"]')
    tag = (By.CSS_SELECTOR,'i[class="el-input__icon el-icon-caret-top"]')# [1]，[3]
    tag_list = (By.CSS_SELECTOR,'li[class="el-select-dropdown__item"]') #标签列表
    add_tag_button = (By.CSS_SELECTOR,'button[class="el-button tag-chose--btn el-button--primary"]') #添加标签按钮
    project_list = (By.CSS_SELECTOR,'p[class="ellipsis"]')
    Agreement_button = (By.CSS_SELECTOR,'span[class="el-checkbox__inner"]')
    EBS_Button = (By.CSS_SELECTOR,'button[class*="el-button--large"]')
    usernameInput = (By.CSS_SELECTOR,'input[placeholder="151xxxxx789/example@didiyun.com"]')
    passwordInput = (By.CSS_SELECTOR,'input[placeholder="8~16位，包含大小写字母、数字、特殊字符"]')
    button = (By.CSS_SELECTOR,'button[class="el-button option-buttom-full success-btn el-button--primary"][type="submit"]')
    check_element = (By.CSS_SELECTOR,'div[class="el-dialog el-dialog--"]')


    def Create_EBS_business(self,username,password,type_name,pay_name,pay_type,EBS_name,xiabiao,tag_name,ject_id,project_name):
        self.driver.get(create_ESB)
        logger.info("_________打开首页__________")
        self.time_sleep(3)
        self.find_Element(*self.a).click()
        self.find_Element(*self.usernameInput).send_keys(username)
        logger.info("_________输入用户名__________")
        self.find_Element(*self.passwordInput).send_keys(password)
        logger.info("_________输入密码__________")
        self.find_Element(*self.button).click()
        logger.info("_________点击登录按钮__________")
        self.time_sleep(6)
        self.find_Element(*self.create_EBS_button).click()
        logger.info("_________点击创建EBS按钮__________")
        self.time_sleep(3)
        self.only_Element(type_name,*self.EBS_type)
        self.time_sleep(3)
        self.only_Element(pay_name,*self.pay)
        self.time_sleep(3)
        self.executE_Script(*self.i)
        self.time_sleep(3)
        self.only_Element(pay_type,*self.pay_type)
        self.find_Element(*self.EBs_name).send_keys(EBS_name)
        self.subscript_Element(xiabiao,*self.tag)
        self.time_sleep(3)
        self.only_Element(tag_name,*self.tag_list)
        self.find_Element(*self.add_tag_button).click()
        self.time_sleep(3)
        self.subscript_Element(ject_id, *self.tag)
        self.time_sleep(3)
        self.only_Element(project_name,*self.project_list)
        #self.find_Element(*self.Agreement_button).click().click()
        self.time_sleep(3)
        logger.info("_________选择项目__________")
        self.find_Element(*self.EBS_Button).click()
        self.time_sleep(7)


    def Check_Create_EBS_C(self):
        if self.find_Element(*self.check_element) != None:
            return True
        else:
            return False


































