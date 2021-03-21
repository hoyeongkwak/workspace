from urllib.request import urlopen
import re
url = 'https://goo.gl/U7mSQl'
html = urlopen(url)
html_content = str(html.read().decode('utf8'))
#print(html_content)
id_list = re.findall(r'[A-Za-z0-9]+\*\*\*', html_content)

for rdata in id_list:
    print(rdata)

