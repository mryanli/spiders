#! -*-codeing:utf-8-*-

from selenium.webdriver.chrome.options import  Options
from selenium import webdriver
import time

#先设置一个浏览器的参数配置对象，第9,10行表示无界面
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#新建一个浏览器对象，改对象加载相应的浏览器配置对象
chrome = webdriver.Chrome(chrome_options=chrome_options)

#浏览器访问页面
chrome.get('https://weibo.com/yaochen?refer_flag=1001030101_&is_hot=1')

#利用xpath抓取页面数据，由于在抓取时有可能相应的页面对象还没有加载完毕
# ，程序会报错，此时需要处理错误，并重新查找，直到找到后，跳出循环
i = 1
while 1:
    try:
        time.sleep(0.5)
        print('tried %d'%i)
        i+=1
        div = chrome.find_element_by_xpath('//*[@id="Pl_Core_Ticket__21"]/div/div/div[3]/div/ul/li/div/div[2]/div[2]/div[2]/a')
        break
    except:
        pass

#打印找到的节点的内部字符
print(div.text)


