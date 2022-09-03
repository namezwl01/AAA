#coding = utf-8
import unittest

import time

from run_testcase.HTMLTestRunnerX import HTMLTestRunner
from test_case.create_ebs_test import EBS_TestCase

from test_case.login_test_case import LoginTestCase
import os
import sys
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTestCase))
    suite.addTests((unittest.TestLoader().loadTestsFromTestCase(EBS_TestCase)))
    #  定义生成测试报告的名称
    filename1 = "../repoets/" + str(time.strftime('%Y%m%d%H%M%S')) + ".html"
    fp = open(filename1, 'wb')
    # 定义测试报告的路径，标题，描述等内容
    runner = HTMLTestRunner(stream=fp, title=u'滴滴云登录', description=u'这是滴滴云登录的测试报告')
    # 执行用例
    runner.run(suite)

