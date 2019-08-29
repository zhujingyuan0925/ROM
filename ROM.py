# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ROM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://192.168.85.202:8802/Default.aspx"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_r_o_m(self):
        driver = self.driver
        driver.get("http://192.168.85.202:8802/Default.aspx")
        driver.find_element_by_xpath("//a[@id='Logoff']/span/span").click()
        driver.find_element_by_xpath("//div[4]/a/span/span").click()
        driver.find_element_by_id("userName").click()
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("107441")
        driver.find_element_by_id("userPwd").clear()
        driver.find_element_by_id("userPwd").send_keys("222222")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("1205")
        driver.find_element_by_xpath("//div[@id='_easyui_tree_270']/span[3]").click()
        driver.find_element_by_id("loginbtn").click()
        driver.find_element_by_xpath("//div[@id='menu']/div[9]/div/div").click()
        driver.find_element_by_xpath("//div[@id='menu']/div[9]/div[2]/ul/li").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=8 | ]]
        driver.find_element_by_xpath("//a[@id='btn_Search']/span/span").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'查看')])[5]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
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
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
