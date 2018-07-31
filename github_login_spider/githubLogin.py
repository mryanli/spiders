#!/usr/bin/python
# -*- coding:UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup

mycli = requests.session()

response = mycli.get('https://github.com/login')
html = response.text
print(response.status_code)
soup = BeautifulSoup(html,'html.parser')

token = soup.find_all('input')[1].attrs.get('value')

data = {
    'commit':'Sign in',
    'utf8':'✓',
    'authenticity_token':token,
    'login':'mryanli',
    'password':'lbhjingji076'
}

new_res = mycli.post('https://github.com/session',data = data)
new_res.encoding='utf-8'
print(new_res.apparent_encoding)
new_html = new_res.text
print(type(new_html))
# print(new_html)
with open('github.html','wb') as f:
    f.write(new_html.encode('utf-8'))













