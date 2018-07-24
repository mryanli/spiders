#!/usr/bin/python
# -*- coding:UTF-8 -*-
from spiders.simple_spyder_implied_by_urllib2 import url_manager, html_downloader, html_parser, data_output


class SpiderMain:
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HTMLDownLoader()
        self.parser = html_parser.HTMLParser()
        self.data_output = data_output.DataOutput()

    def craw(self,root_url  ):
        self.urls.add_new_url(root_url)
        while self.has_new_url():
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)
            new_urls,new_data = self.parser.parse(new_url,html_cont)
            self.urls.add_new_urls(new_urls)
            self.data_output.collect_data(new_data)

        self.data_output.output_html()

    def has_new_url(self):
        pass


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/网络爬虫'
    spider = SpiderMain()
    spider.craw(root_url)
