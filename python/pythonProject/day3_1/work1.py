import re
from urllib.request import urlopen

url = 'https://www.hanbit.co.kr/store/books/full_book_list.html'
html = urlopen(url)
html_content = html.read().decode('utf-8')
#print(html_content)

#book_list_table = re.findall(r'(\<div class\=\"table_area\"\>([\s\S]+?)\<\/div\>)',html_content)
#print(book_list_table)

#book_list = re.findall(r'(\<tr\>([\s\S]+?)\<\/tr\>)', str(book_list_table))
book_list_table = re.findall(r'(\<tbody\>([\s\S]+?)\<\/tbody\>)', str(html_content))

book_list = re.findall(r'(\<tr\>([\s\S]+?)\<\/tr\>)', str(book_list_table))
#print(book_list)


for idx in book_list:
    #book = re.findall(r'(\<td class\=\"left\"\>(\<a href\=[\s\S]+?\<\/a\>)\<\/td\>)', str(idx))
    book = re.findall(r'\<a href=(".*?")', str(idx))
    bookname = re.findall(r'\<a href=".*?">([\s\S]+?)\<\/a\>', str(idx))
    print("==========================================")
    print("URL : " + "http://" + book[0])
    print("name : " + bookname[0])
    print("==========================================")

