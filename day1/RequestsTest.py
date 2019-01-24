# -*- coding: utf-8 -*-

import requests
import json

url = "http://fanyi.baidu.com/v2transapi"

params = {
    "form":"en",
    "to":"zh",
    "query":"test"}
print('打印前')
r = requests.request("post",url,params=params)
print(r)
print(r.text)
print('打印后')

print(r.url)
print(r.encoding)
d = json.loads(r.text)
#print(d.json())
#print(d['liju_result']['tag'])