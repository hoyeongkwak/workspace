import dload
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

searchStr = input('찾을 이미지 이름: ')

baseUrl = 'https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q='
url = baseUrl + quote_plus(searchStr)
#print(url)

driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
time.sleep(5)

html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')

thumbnails = bsObj.select('#imgList > div > a > img')
#print(thumbnails)

for i, thumbnails in enumerate(thumbnails):
    src = thumbnails['src']
    dload.save(src, f'imgs/{i}.jpg') # == "imgs/{}.jpg".format(i)

driver.quit()