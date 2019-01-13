
# import unittest
# test_dir= r'D:\应用软件\pycharm\PyCharm Community Edition 2018.3\PycharmProjects\untitled\ttt-001\BASE'
# test_case=unittest.TestSuite()
# discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern="test_Babel.py",top_level_dir=None)
#
# test_case.addTests(discover)
# runner=unittest.TextTestRunner()
# runner.run(test_case)

import unittest
import HTMLTestRunner
import time
import smtplib

test_dir = r'D:\应用软件\pycharm\PyCharm Community Edition 2018.3\PycharmProjects\untitled\ttt-001\BASE'
test_case= unittest.TestSuite()
discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py',top_level_dir=None)
test_case.addTests(discover)

#生成测试报告，注意‘：’在python里面属于特殊字符，不能用
now=time.strftime("%Y-%m-%d %H_%M_%S")
report_file=r'D:\应用软件\pycharm\PyCharm Community Edition 2018.3\PycharmProjects\untitled\ttt-001\report\%s-report.html' %now
fp = open(report_file, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp ,title=u"测试报告",description=u"这个是描述")
runner.run(discover)
fp.close()

# import unittest
# import HTMLTestRunner
# import time
#
# case_dir=r'D:\应用软件\pycharm\PyCharm Community Edition 2018.3\PycharmProjects\untitled\ttt-001\BASE'
# test_case = unittest.TestSuite()
# discover = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='test*.py',top_level_dir=None)
# test_case.addTests(discover)
#
# now=time.strftime("%Y-%m-%d %D-%M-%S")
# report_file=r'D:\应用软件\pycharm\PyCharm Community Edition 2018.3\PycharmProjects\untitled\ttt-001\report\%s-result.html'%now
# fp =open(report_file,"wb")
# runner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="这是报告",description="这是描述")
# runner.run(test_case)
# fp.close()