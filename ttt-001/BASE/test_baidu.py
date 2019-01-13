# coding: utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import unittest
class TestBaidu(unittest.TestCase):
    def setUp(self):
    #加载启动项
        option=webdriver.ChromeOptions()
        option.add_argument("disable-infobars")
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(2)
    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("JD")
        time.sleep(2)
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.driver.back()

        self.driver.find_element_by_name("tj_trtieba").click()
        time.sleep(2)
        self.driver.find_element_by_name("kw1").send_keys("JD")
        self.driver.find_element_by_partial_link_text("进入贴吧").click()
        time.sleep(2)

        mouse=self.driver.find_element_by_class_name("u_member_wrap")
        ActionChains(self.driver).move_to_element(mouse).perform()
        time.sleep(2)
        self.driver.find_element_by_class_name("dropdown-tbmall").click()
        time.sleep(3)
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()

