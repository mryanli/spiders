#!/usr/bin/python
# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse
import chardet

class HTMLParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r'/item/'))
        for link in links:
            new_full_url = urlparse.urljoin('https://baike.baidu.com',link['href'])
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self,page_url,soup):
        res_data = {}
        title_node = soup.find('dd',class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['url'] = page_url
        res_data['title'] = title_node.get_text()
        digest_node = soup.find('div',class_='lemma-summary').find('div',class_='para')
        res_data['digest'] = digest_node.get_text()
        print(digest_node.get_text().encode('utf8'))



        return res_data
