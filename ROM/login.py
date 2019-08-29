#coding=utf-8
#author：zhujingyuan
from selenium import  webdriver
import time
import unittest
import selenium


browser=webdriver.Chrome()
browser.get("http://192.168.85.202:8802/Default.aspx")

# 将浏览器最大化显示
browser.maximize_window()
print "浏览器最大化"
browser.find_element_by_id("userName").send_keys("107441")
browser.find_element_by_id("userPwd").send_keys("222222")
browser.find_element_by_xpath("/html/body/form/div[2]/div/fieldset/p[3]/span/span/span/a").click()
browser.find_element_by_xpath("/html/body/div[1]/div/ul/li[4]/ul/li[2]/ul/li[1]/ul/li[5]/div/span[6]").click()
browser.find_element_by_id("loginbtn").click()
time.sleep(3)

#获取用户名
loginname=browser.find_element_by_id("lbUserName").text

if loginname==u'朱静源':
    print '登录成功'
else:
    print 'user name error!'




