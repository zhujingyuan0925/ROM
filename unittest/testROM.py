# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re    # 引入unittest 框架包
import HTMLTestRunner

class ROMChrome(unittest.TestCase):
    #ROMChrome类继承unittest.TestCase 类，从TestCase 类继承是告诉unittest 模块的方式，这是一个测试案例。
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL 的访问放到初始化部分。
    def test_r_o_m_chrome(self):
        driver = self.driver
        driver.get("http://192.168.85.202:8802/Login.aspx")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_id("userName").clear()
        time.sleep(2)
        driver.find_element_by_id("userName").send_keys("107441")
        time.sleep(2)
        driver.find_element_by_id("userPwd").send_keys("222222")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/form/div[2]/div/fieldset/p[3]/span/span/span/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/ul/li[4]/ul/li[2]/ul/li[1]/ul/li[5]/div/span[6]").click()
        time.sleep(2)
        driver.find_element_by_id("loginbtn").click()
        time.sleep(2)
        # driver.find_element_by_link_text(u"订单管理列表").click()

        #test_r_o_m_chrome中放置的就是我们的测试脚本

    def test_r_o_m_firefox(self):
        driver = self.driver
        driver.get("http://192.168.85.202:8802/Login.aspx")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("107441")
        driver.find_element_by_id("userPwd").send_keys("222222")
        driver.find_element_by_xpath("/html/body/form/div[2]/div/fieldset/p[3]/span/span/span/a").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/ul/li[4]/ul/li[2]/ul/li[1]/ul/li[5]/div/span[6]").click()
        driver.find_element_by_id("loginbtn").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

       #is_element_present 函数用来查找页面元素是否存在

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

       #对弹窗异常的处理
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

        #关闭警告以及对得到文本框的处理
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

        #tearDown 方法在每个测试方法执行后调用，这个地方做所有测试用例执行完成的清理工作，如退出浏览器等。


if __name__ == "__main__":
     #unittest.main()    #unitest.main()函数用来测试类中以test 开头的测试用例

     suit=unittest.TestSuite()
     suite.addTest(ROMChrome("test_r_o_m_chrome"))    #添加测试用例集
     suite.addTest(ROMChrome("test_r_o_m_firefox"))
     runner=unittest.TextTestRunner()
     runner.run(suite)    #执行测试
