from bs4 import BeautifulSoup

#file = open('books.xml', 'r', encoding='utf8') 아래와 동일
with open('books.xml', 'r', encoding='utf8') as file:
    book_xml = file.read()

#print(book_xml)

bsObj = BeautifulSoup(book_xml, 'lxml')
#print(bsObj)

for book_info in bsObj.findAll('author'):
    print(book_info.text)

