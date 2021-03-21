'''
1. 공공데이터포털 사이트의 전국 약국 정보 조회 서비스 데이터를 이용하여 코드를 진행하시오
  ㄱ. 서울특별시에 있는 약국 데이터만 사용한다
  ㄴ. 파라미터 일부는 다음과 같다
       ORD='NAME',  pageNo='1', numberOfRows='5000'
  ㄷ. 가져온 데이터에서 월요일 오후9시 넘어서까지 운영하는 약국의 수를 출력하시오
'''
from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'jcIDt4PJUiyQbVi14kCIL5rsq5i80l605%2FQ3TgBUlOp8I3qqrQt472uuqTPSIBL2CDvpA09wHbpr6hs3%2BCrOjg%3D%3D'

Q0 = quote_plus('서울특별시')
ORD = 'NAME'
pageNo = '1'
numOfRows = '5000'

parameter = 'serviceKey=' + serviceKey + '&Q0=' + Q0 + '&ORD=' + ORD + '&pageNo=' + pageNo + '&numOfRows=' + numOfRows
url = endpoint + parameter
#print(url)

request = requests.get(url)
bsObj = BeautifulSoup(request.content, 'lxml')
item = bsObj.findAll('item')

nCount = 0
for item in bsObj.findAll('dutytime1c'):
    if int(item.text) > 2100:
        nCount += 1

print(nCount)