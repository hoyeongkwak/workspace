'''
1. 대상 사이트 jolse.com 사이트((http://www.jolse.com/)를 이용합니다.
2.메인페이지에서 상단 메뉴중에 SKINCARE -> Moisturizers -> Toners & Mists로 이동합니다.
3. 이동한 화면에서 화장품들의 이름과 가격 정보를 수집합니다.
4. 위의 데이터 수집은 1페이지 부터 5페이지까지 진행합니다.
5. 이 때 항목 선택을 위해 사용하는 코드와 출력부 코드 부분을 함수화 합니다.
6. 출력 결과는 아래와 같이 합니다.
  [출력 결과]
  Isntree Hyaluronic Acid Toner 200ml (Renewal),USD 19.00
  ETUDE HOUSE Soon Jung pH 5.5 Relief Toner 180ml,USD 18.57
  SON&PARK; BEAUTY WATER 340ml,USD 29.40
  SOME BY MI AHA BHA PHA 30 Days Miracle Toner 150ml,USD 22.20
  SOME BY MI Galactomyces Pure Vitamin C Glow Toner 200ml,USD 21.20
  PURITO Centella Green Level Calming Toner 200ml,USD 23.07
  SON&PARK; Beauty Water 60ml,USD 10.50
     .
     .
     .
     .
     .
  skin79 Jeju Aloe Aqua Toner 150ml,USD 14.00
  skin79 Golden Snail Intensive Toner 130ml,USD 27.00
  reduire Trouble Relieving Time Toner 200ml,USD 19.00
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('chromedriver.exe')
url = 'http://www.jolse.com/'
driver.get(url)
time.sleep(3)
prod_data_total = []

def mouseroverElement(title):
    element = driver.find_elements_by_link_text(title)[0]
    ActionChains(driver).move_to_element(element).perform()
    return element

mouseroverElement('SKINCARE')
mouseroverElement('Moisturizers')
mouseroverElement('Toners & Mists').click()

def get_search_page_url(page):
    return 'https://www.jolse.com/category/toners-mists/1019/?page={}'.format(page)

def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        try:
            title = prod_item.select('p.name > a > span')[0].text.strip()
        except:
            title=''
        try:
            origin_price = prod_item.select('ul > li')[0].text.strip().replace('Price ', '')
        except:
            origin_price=''
        try:
            sale_price = prod_item.select('ul > li')[1].text.strip()
        except:
            sale_price=''
        prod_data.append([title, origin_price, sale_price])
    return prod_data

for page in range(1, 5):
    url = get_search_page_url(page)
    driver.get(url)
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    prod_items = soup.select('div.xans-element- > ul.prdList > li.item > div.box > div.description > div.fadearea')

    prod_item_list = get_prod_items(prod_items)
    prod_data_total = prod_data_total + prod_item_list

#print(prod_data_total)
for item in prod_data_total:
    print(item[0] + " " + item[1])
