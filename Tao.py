from selenium import webdriver
import os

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)


url = "http://www.taolivingconcept.com/"
browser.get(url)

browser.find_element_by_xpath('//*[@id="header"]/div/div[2]/ul/li[8]/a').click()

windows = browser.current_window_handle

all_handles = browser.window_handles
for handle in all_handles:
    if handle != windows:
        browser.switch_to.window(handle)

browser.find_element_by_class_name('goods-thumb').click()

num = browser.window_handles
browser.switch_to.window(num[2])

browser.find_element_by_xpath('//*[@id="goodsDetail"]/div[2]/div[3]/div[3]/a[1]').click()

browser.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[2]/a').click()

browser.find_element_by_xpath('//*[@id="btnCheckOut"]').click()

browser.find_element_by_xpath('//*[@id="UserName"]').send_keys("15158027703")

browser.find_element_by_xpath('//*[@id="Password"]').send_keys("qw87758258")

browser.find_element_by_xpath('//*[@id="btnLogin"]').click()

# browser.find_element_by_xpath('/html/body/div[3]/div/div').click()
browser.find_element_by_class_name('closes').click()

browser.find_element_by_xpath('//*[@id="btnCheckOut"]').click()

browser.find_element_by_xpath('//*[@id="deliverylist"]/label[1]/input').click()

browser.find_element_by_xpath('//*[@id="DivConfirmOrderSP"]/div[3]/div[3]/p[2]/a[2]').click()

browser.find_element_by_xpath('//*[@id="payconfirm"]/div/div[4]/dl[1]/dd/label/input').click()

browser.find_element_by_xpath('//*[@id="btnSubmit"]').click()







