

import requests
headers = {
'Referer': 'https://www.baidu.com/link?url=kE-6fr0sL7obbCT3fekWnHFMGioMgfQRdal6fRdszLy&wd=&eqid=9a079b1d00010ed6000000055b6a5310',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}
response = requests.get('https://weibo.com/')
response.encoding = response.apparent_encoding

data = response.text

print(data)