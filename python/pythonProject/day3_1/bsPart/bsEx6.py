from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.naver.com/'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')

start_page = bsObj.find('div', {'class':'service_area'})
#print(start_page)

first_atag = start_page.find('a')
#print(first_atag)
#print(first_atag.text)
#print(first_atag['href'])

navi_menu = bsObj.find('ul', {'class':'list_nav'})
#print(navi_menu)
litag = navi_menu.findAll('li')
#print(litag)

nameList = []

for idx in litag:
    nameList.append(idx.text)
print(nameList)