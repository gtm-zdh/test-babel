from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
#加载启动项
option=webdriver.ChromeOptions()
option.add_argument("disable-infobars")

driver = webdriver.Chrome(options=option)
driver.get("https://m.jd.co.th/")
driver.maximize_window()
time.sleep(3)

driver.refresh()
time.sleep(2)
driver.find_element_by_xpath("//*[@class='login active']").click()
time.sleep(2)
driver.find_element_by_id("login-username").send_keys("gaotianming3@jd.com")
driver.find_element_by_id("login-password").send_keys("Zwy19920622!")
time.sleep(3)
driver.find_element_by_id("login-btn").click()
time.sleep(2)

Lang=driver.find_element_by_xpath("//*[@class='slogan-icon th']")
ActionChains(driver).move_to_element(Lang).perform()
driver.find_element_by_xpath("//*[@class='en lang']").click()
time.sleep(3)
driver.quit()

