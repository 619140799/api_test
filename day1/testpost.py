# -*- coding: utf-8 -*-

import requests
from pip._internal import req
from wx._core import HD_ALLOW_REORDER
from requests import Request,Session

#r = requests.get('https://api.github.com/some/endpoint')
#print(r.status_code) #响应状态码
#print(r.status_code==requests.codes.__subclasshook__()) #内置状态码查询对象
#r.raise_for_status() #通过Response.raise_for_status()来抛出异常


#a = requests.get('http://httpbin.org/get')
#print(a.headers) #获得响应头信息
#print(a.headers['Content-Type'])
#print(a.headers.get('Content-Length'))
#print(a.cookies)


#r = requests.get('https://api.douban.com/v2/book/search?小王子')
#print(r.cookies)
#print(r.cookies['bid'])

#url = 'http://httpbin.org/cookies'
#cookies = dict(cookies_are='Working')
#a = requests.get(url, cookies=cookies)
#print(a.text)
'''
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie','yum',domain='httpbin.org',path='/cookies')
jar.set('gross_cookie','blech',domain='httpbin.org',path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)
'''

##重定向
'''
r = requests.get('http://github.com')
print(r.history)
'''

#通过allow_redirects参数禁用重定向处理
'''
r = requests.get('http://github.com', allow_redirects=False)
print(r.url)
print(r.status_code)
print(r.history

#使用head重启重定向
r = requests.get('http://github.com', allow_redirects=True)
print(r.url)
print(r.status_code)
print(r.history)
'''

s = Session()
url = 'https://api.douban.com/v2/book/search'
data={'q':'小王子'}
header={'User-Agent':''}