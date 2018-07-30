#!/usr/bin/python
# -*- coding:UTF-8 -*-
#python  2.7

import url_manager, html_downloader, html_parser, data_output


class SpiderMain:

    def __init__(self):

        self.url = url_manager.UrlManager()
        self.downloader = html_downloader.HTMLDownLoader()
        self.parser = html_parser.HTMLParser()
        self.data_output = data_output.DataOutput()

    def craw(self,root_url  ):
        self.url.add_new_url(root_url)
        count = 1
        while self.url.has_new_url():
            try:
                new_url = self.url.get_new_url()
                print('craw %d : %s'%(count,new_url.decode('UTF8').encode('utf-8')))
                html_cont = self.downloader.download(new_url)

                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.url.add_new_urls(new_urls)
                self.data_output.collect_data(new_data)
                if count ==10:
                    break

                count +=1
            except Exception as e:
                print('craw failed...')

        self.data_output.output_html()

    def has_new_url(self):
        pass


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/网络爬虫'
    spider = SpiderMain()
    spider.craw(root_url)
