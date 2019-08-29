#coding=utf-8
#author：zhujingyuan
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
        # WebDriverWait(driver, timeout, poll_frequency=3, ignored_exceptions=None)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://hh.yologoer.com/roomideas.shtml?bcid=bb243cb8-87c5-4418-8b07-245bd8cd3a4b")
        driver.maximize_window()
        # driver.WebDriverWait(driver, timeout, poll_frequency=3, ignored_exceptions=None)
        time.sleep(3)
        driver.find_element_by_link_text(u"灵感居室").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"热卖商品").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"所有商品").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"方案中心").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"视频中心").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"会员中心").click()
        time.sleep(3)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
