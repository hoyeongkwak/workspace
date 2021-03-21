from bs4 import BeautifulSoup

with open('US08621662-20140107.XML', 'r', encoding='utf8') as file:
    us_xml = file.read()

bsObj = BeautifulSoup(us_xml, 'lxml')

for invention in bsObj.findAll('invention-title'):
    print(invention.text)