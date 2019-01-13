# coding :utf-8

from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class TestBabel(unittest.TestCase):
    u'''注释可以加在这里'''
    def login(self):
        self.driver.find_element_by_xpath("//*[@class='a-login']").click()
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys("gaotianming4")
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys("Zwy19920622!")
        self.driver.find_element_by_xpath("//*[@class='formsubmit_btn']").click()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

    def setUp(self):
        # 加启动配置
        option = webdriver.ChromeOptions()
        option.add_argument("disable-infobars")

        self.driver = webdriver.Chrome(options=option)
        self.driver.get("http://beta-babel.jd.co.th/active/operation/srcIntl/zh_CN/module/login/index.html")
        time.sleep(2)
        self.driver.maximize_window()  # 设置浏览器大小，全屏

    def test_creatjob(self):
        u'''这是创建项目的代码'''
        self.login()
        t = self.driver.title
        print(t)
        self.assertEqual(t, "项目列表-运营开发平台")
        self.driver.find_element_by_xpath("//*[text()='新建项目']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='pt c_stat']").send_keys("babel-test")
        # 用js 取消readonly属性
        js = 'document.getElementsByClassName("d-pt d-sdt")[0].removeAttribute("readonly");'
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath("//*[@class='d-pt d-sdt']").send_keys("2018-12-6 00:00:00")
        time.sleep(3)

        # 输入时间的第二种方法
        js1 = 'document.getElementsByClassName("d-pt d-sdt")[1].removeAttribute("readonly");'
        self.driver.execute_script(js1)
        # driver.find_element_by_xpath("//div[@class='d-pt d-sdt'][2]").send_keys("2024-12-6 00:00:00")
        value = 'document.getElementsByClassName("d-pt d-sdt")[1].value="2024-12-6 00:00:00"'
        self.driver.execute_script(value)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
