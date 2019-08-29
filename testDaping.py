# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Daping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_daping(self):
        driver = self.driver
        driver.get("http://192.168.18.163:9017/roomideas.shtml?bcid=82045d2e-b713-4b00-88e3-cbde94338376")
        driver.find_element_by_link_text(u"热卖商品").click()

        time.sleep(5)

        # driver.find_element_by_css_selector("a.goods_list_imgbox > img").click()
        #
        # time.sleep(5)
        #
        # driver.find_element_by_xpath("//dl[2]/dt").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='数量'])[1]/preceding::p[1]").click()
        # driver.find_element_by_id("number").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='宽51X长51CM'])[2]/following::dt[2]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='数量'])[1]/following::p[5]").click()
        # driver.find_element_by_xpath(
        #     u"(.//*[normalize-space(text()) and normalize-space(.)='数量'])[1]/following::span[1]").click()
        # driver.find_element_by_xpath(
        #     "(.//*[normalize-space(text()) and normalize-space(.)='SALE'])[1]/preceding::img[1]").click()
        #
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
