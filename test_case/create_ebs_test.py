#coding = utf-8
import os
import sys
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from businessPage.create_ebs import Create_EBS_C
from common.Myunit import MyUnit

class EBS_TestCase(MyUnit):

    def testCreatEBS_1(self):
        C = Create_EBS_C(self.driver)
        C.Create_EBS_business("17600570787","3edc@WSX","高效云盘","≈0.60元/天","按时长","QAtest",1,"请勿删除",3,"回归测试")
        self.assertTrue(C.Check_Create_EBS_C(),True)

    def testCreatEBS_2(self):
        C = Create_EBS_C(self.driver)
        C.Create_EBS_business("17600570787","3edc@WSX","SSD云盘","≈8.00元/天","按时长","AA",1,"请勿删除",3,"回归测试")
        self.assertTrue(C.Check_Create_EBS_C(),True)


if __name__ == '__main__':
    MyUnit.main()