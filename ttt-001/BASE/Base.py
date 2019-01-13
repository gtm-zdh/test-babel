#coding: utf-8
from selenium import webdriver
import time
# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument("disable-infobars")

driver= webdriver.Chrome(options=option)
driver.get("https://m.jd.co.th/")
time.sleep(5)
driver.maximize_window()   #设置浏览器大小，全屏

time.sleep(5)
#driver.find_element_by_class_name("close_btn").click()
driver.find_element_by_xpath("//span[class='close_btn']/div")

time.sleep(3)
driver.quit()

