#coding=utf-8

'''
Created on 2019年1月23日

@author: QINGYUAN
'''
import datetime
from selenium import webdriver
import time

'''
now_time = datetime.datetime.now().strftime('%Y-%m-%d')
print(type(now_time))
'''


url = 'https://xueqiu.com/hq#exchange=CN&firstName=1&secondName=1_0&page=1'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
cookie = driver.get_cookies()
#print(cookie)
cookietemp=''
for i in cookie:
    #print('%s=%s;'%(i['name'],i['value']))
    cookietemp=cookietemp+i['name']+':'+i['value']+';'
    
print(cookietemp)
print(cookietemp[:-1])
driver.quit()