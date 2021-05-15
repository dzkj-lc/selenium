from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys

options =webdriver.ChromeOptions()
options.add_argument('–log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.binary_location="C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

class TestCase():
    def setup_class(self):
        driver.get("https://www.baidu.com/")
    def teardown_class(self):
        driver.close()
    def setup(self):
        print("\nsetup: 每个用例开始前都会执行")
        sleep(3)
    def teardown(self):
        print("\nteardown: 每个用例结束后执行")
        sleep(3)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

    def test_One(self):
        driver.find_element_by_id("kw").send_keys(("Test search"))  #空格
        driver.find_element_by_id("su").click()
    def test_Two(self):
        driver.find_element_by_id("kw").send_keys(("@#￥%……&"))#特殊字符
        driver.find_element_by_id("su").click()
    def test_Three(self):
        driver.find_element_by_id("kw").send_keys(("12345678"))#整数
        driver.find_element_by_id("su").click()