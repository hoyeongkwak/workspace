from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naver.com')
time.sleep(2)

login_btn = driver.find_element_by_class_name('ico_naver')
login_btn.click()
time.sleep(2)

tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('pw')

tag_id.clear()
time.sleep(2)

import pyperclip
tag_id.click()
pyperclip.copy('hamolf')
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

tag_pw.click()
pyperclip.copy('Happy001$')
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

login_btn = driver.find_element_by_id('log.login')
login_btn.click()

from bs4 import BeautifulSoup

driver.get('https://order.pay.naver.com/home')
html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')
print(bsObj)