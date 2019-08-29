#coding=utf-8
#author：zhujingyuan

from selenium import webdriver
import time

browser =webdriver.Chrome()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
# time.sleep(10)
# driver.implicitly_wait(10)
browser.find_element_by_id("su").click()

print "浏览器最大化"
browser.maximize_window() #将浏览器最大化显示

# browser.quit()