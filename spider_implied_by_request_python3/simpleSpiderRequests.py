#!/usr/bin/python
# -*- coding:UTF-8 -*-

import requests
import UserAgent
import random

for i in range(10):
    header ={'User-Agent':random.choice(UserAgent.user_agent)}
    response = requests.get('http://www.sina.com.cn',headers=header)
    # print(response.)
    response.encoding = 'utf-8'
    print(header['User-Agent'])


