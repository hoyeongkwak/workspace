from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')

bsobj = BeautifulSoup(html, 'html.parser')

for link in bsobj.find('div',{'id':'bodyContent'}).findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])