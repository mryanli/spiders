#!/usr/bin/python
# -*- coding:UTF-8 -*-

from concurrent.futures import ProcessPoolExecutor
import requests

'''
方法1，多进程，进程自身处理结果，即在任务函数内处理线程返回的结果
注意：用多进程时，由于一个进程就是一个py文件的运行，多进程就是
多个一模一样的py文件运行，但是进程是有父进程和子进程的区别的，而电脑是通过
if __name__ == '__main__'语句来区别父进程和子进程的，所以需要在父进程中
加入上述判断语句来区分，否则会出错。
'''

pool = ProcessPoolExecutor(10)

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


if __name__ == '__main__':


    for url in url_lists:
        pool.submit(task,url)

    pool.shutdown(wait = True)






