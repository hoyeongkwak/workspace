import requests

params = { 'username':'Ryan', 'password':'password'}

rp = requests.post('http://pythonscraping.com/pages/cookie/welcome.php', params)
print(rp.cookies.get_dict())

rp = requests.get('http://pythonscraping.com/pages/cookie/profile.php', cookies=rp.cookies)
print(rp.text)