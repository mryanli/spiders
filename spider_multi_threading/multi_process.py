#!/usr/bin/python
# -*- coding:UTF-8 -*-

from concurrent.futures import ProcessPoolExecutor
import requests

'''
方法1，多进程，进程自身处理结果，即在任务函数内处理线程返回的结果
'''

pool = ProcessPoolExecutor(6)

url_lists = [
     'http://www.sina.com.cn',
     'http://www.qq.com',
     'http://www.163.com',
     'http://www.sogou.com',
     'http://www.xici.com'
    ]

def task(url):
    response = requests.get(url)
    print(url,response)

for url in url_lists:
    pool.submit(task,url)
    pool.shutdown(wait = True)






