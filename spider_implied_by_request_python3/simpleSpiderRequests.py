#!/usr/bin/python
# -*- coding:UTF-8 -*-

import requests
from UserAgent import user_agent
import random
for i in range(10):
    header ={'User-Agent':random.choice(user_agent)}
    response = requests.get('http://www.sina.com.cn',headers=header)
    response.encoding = 'utf-8'
    print(header['User-Agent'])


