from selenium import webdriver
import time


def openchrome():
    bro = webdriver.Chrome()
    bro.get('http://www.baidu.com')
    time.sleep(1)
    # bro.find_element_by_xpath('//*[@id="home"]/div[1]/div[2]/div[1]/div[4]/span/span').click()
    # bro.save_screenshot('indexbaidu.png')
    # account = 'liubaohua8801'
    # password = 'lbh85903953'
    # while True:
    #     try:
    #         bro.find_element_by_xpath('//*[@id="home"]/div[1]/div[2]/div[1]/div[4]/span/span').click()
    #         break
    #     except:
    #         continue
    # time.sleep(5)
    # while 1:
    #     try:
    #         bro.find_element_by_id('TANGRAM__PSP_4__userName').send_keys(account)
    #         break
    #     except:
    #         continue
    #
    # while 1:
    #     try:
    #         bro.find_element_by_id('TANGRAM__PSP_4__password').send_keys(password)
    #         break
    #     except:
    #         continue
    #
    # while 1:
    #     try:
    #         bro.find_element_by_id('TANGRAM__PSP_4__submit').click()
    #         break
    #     except:
    #         continue

    # bro.close()

openchrome()