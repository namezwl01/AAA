#coding = utf-8
from common.Myunit import MyUnit
from businessPage.loginPage import LoginPage
#from businessPage import LoginPage
from common.selenium_and_driver import logger

import os
import sys
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

class LoginTestCase(MyUnit):
    file_path = "../data/user.csv"
    def testLogin1(self):
        L = LoginPage(self.driver)
        L.Login_business("17600570787","3edc@WSX")
        self.assertTrue(L.check_login(),True)


    def testLogin2(self):
        L = LoginPage(self.driver)
        row = L.getCsvDataByLine(csv_file=self.file_path,line=1)
        logger.info(row)
        L.Login_business(row[0],row[1])
        self.assertTrue(L.check_login(),True)
if __name__ == '__main__':
    MyUnit.main()





