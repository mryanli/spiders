#!/usr/bin/python
# -*- coding:UTF-8 -*-

import urllib2
class HTMLDownLoader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()

if __name__ == '__main__':

    root_url = 'https://baike.baidu.com/item/网络爬虫'

    dow = HTMLDownLoader()
    con = dow.download(root_url)

    print(con)