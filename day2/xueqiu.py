#coding=utf-8
'''
Created on 2019年1月22日

@author: QINGYUAN
'''


from urllib import request
import json
from selenium import webdriver
import time
from day2.cxOracleConnent import Ora
import datetime

url = 'https://xueqiu.com/hq#exchange=CN&firstName=1&secondName=1_0&page=1'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)


pagetatol = driver.find_element_by_xpath('//ul[@class="pager"]/li[8]/a').text
cookie = driver.get_cookies()
#print(cookie)
cookietemp=''
for i in cookie:
    #print('%s=%s;'%(i['name'],i['value']))
    cookietemp=cookietemp+i['name']+'='+i['value']+';'
cookielast=cookietemp[:-1]  
print(cookielast)
print(pagetatol)
driver.quit()
#i = 1 #记录第一个ajax请求
page = 1  #记录当前页
size = 30 #每页显示多少条数据
#定义表列名
columns = ['symbol','gpname','gpcurrent','gppercent','gpchange','gphigh','low','high52w','low52w','marketcapital','amount','gptype','pettm','volume','hasexist']
#定义连接字符串
db_info = {
        'dbtype':'oracle',
        'user':'system',
        'pwd':'Xin@177188',
        'host':'localhost',
        'port':'1521',
        'sid':'orcl'
        } 
orc = Ora(db_info=db_info)

values = []
symbol = [] 
name = [] 
current = [] 
percent = [] 
change = [] 
high = [] 
low = [] 
high52w = [] 
low52w = [] 
marketcapital = [] 
amount = [] 
gptype = [] 
pettm = [] 
volume = [] 
hasexist = []
while page <= int(pagetatol):
    print('page:%s'%(page))
    base_url = "https://xueqiu.com/stock/cata/stocklist.json?page={}&size={}&order=desc&orderby=percent&type=11%2C12".format(page,size)
    #print(base_url)
    head={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Cookie":"%s"%(cookielast),
        }  
      
    req =request.Request(url=base_url,headers=head)
    res = request.urlopen(req)
    base_data=res.read().decode("utf-8")
    new_data = json.loads(base_data)
    #print(new_data)
    for i in new_data["stocks"]:
        # print(i)
        symbol.append(i['symbol'])
        name.append(i['name']) 
        current.append(i['current'])
        percent.append(i['percent']) 
        change.append(i['change']) 
        high.append(i['high']) 
        low.append(i['low']) 
        high52w.append(i['high52w']) 
        low52w.append(i['low52w']) 
        marketcapital.append(i['marketcapital']) 
        amount.append(i['amount']) 
        gptype.append(i['type']) 
        pettm.append(i['pettm']) 
        volume.append(i['volume']) 
        hasexist.append(i['hasexist'])
        #print(symbol)
        '''with open("./雪球.json","a+",encoding="utf-8") as f:
            f.write(json.dumps(i,ensure_ascii=False)+"\n")'''
       
    page += 1
#print('最后一个值：%s'%(symbol[len(symbol)-1]))
#print(columns)
#获取当前日期
#now_time = datetime.datetime.now().strftime('%Y-%m-%d')
j = 0
k = len(symbol) -1
for j in range(k):
    value = (symbol[j],name[j],current[j],percent[j],change[j],high[j],low[j],high52w[j],low52w[j],marketcapital[j],amount[j],gptype[j],pettm[j],volume[j],hasexist[j])
    values.append(value)
    #print(value)
    #print(j)
orc.multi_insert('gplist', columns, values)
#print(values)