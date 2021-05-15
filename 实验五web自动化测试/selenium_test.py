from time import sleep
from selenium import webdriver
import pytest

options =webdriver.ChromeOptions()
options.binary_location="C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get("https://www.baidu.com/")
sleep(3)
driver.find_element_by_id("kw").send_keys(("Test search"))
driver.find_element_by_id("su").click()
sleep(3)
driver.quit()
