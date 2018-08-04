#!/usr/bin/python
# -*- coding:UTF-8 -*-

from concurrent.futures import ThreadPoolExecutor
import requests

'''
方法1，多线程，线程自身处理结果，即在任务函数内处理线程返回的结果
'''

pool = ThreadPoolExecutor(3)

url_lists = [
     'http://www.baidu.com',
     'http://www.baidu.com',
     'http://www.baidu.com',
     'http://www.baidu.com',
     'http://www.baidu.com',
     'http://www.baidu.com',
     'http://www.baidu.com',
     'http://www.sina.com.cn',
     'http://www.qq.com',
     'http://www.163.com',
     'http://www.sogou.com',
     'http://www.xici.com'
    ]

def task(url):
    response = requests.get(url)
    return response   #此处不打印，直接返回函数结果

def done1(future,*args,**kwargs):
    print(future.result())

def done2(*args,**kwargs):
    print('i am done2')

for url in url_lists:
    thread= pool.submit(task,url) #用thread来拿到线程
    thread.add_done_callback(done1) #在线程上调用回调函数，好处是可以调用多个回调函数

    thread.add_done_callback(done2)


pool.shutdown(wait = True)





