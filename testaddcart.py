# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://hh.yologoer.com/roomideas.shtml?bcid=bb243cb8-87c5-4418-8b07-245bd8cd3a4b")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element_by_link_text(u"所有商品").click()
        time.sleep(3)
        a=driver.find_element_by_xpath("/html/body/div[8]/img[1]")
        driver.execute_script("$(arguments[0]).click()", a)
        time.sleep(3)

        b=driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='卧室织物'])[1]/following::div[1]")

        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='卧室织物'])[1]/following::div[1]")
        driver.execute_script("$(arguments[0]).click()", b)
        time.sleep(3)

        driver.find_element_by_xpath("/html/body/div[7]/div/div/div[4]/div/ul/li/a").click()
        time.sleep(3)


        driver.find_element_by_xpath("//ul[@id='goods_list']/li[12]/div/i").click()
        # driver.find_element_by_xpath("/html/body/div[7]/div[1]/div/ul/li[12]/div/i").click()
        # c=driver.find_element_by_xpath("/html/body/div[7]/div[1]/div/ul/li[3]/a/img")
        # driver.execute_script("$(arguments[0]).click()", c)
        time.sleep(5)


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
