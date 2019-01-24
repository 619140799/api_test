#coding=utf-8
'''
Created on 2019年1月22日

@author: QINGYUAN
'''
import requests
from lxml import etree
import json
import time

url = {'''
    'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=111',
    'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=184275&count=15&category=111',
    'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=184086&count=15&category=111','''
    'https://xueqiu.com/stock/cata/stocklist.json?page=1&size=30&order=desc&orderby=percent&type=11%2C12&_=1548157977631'
}


#请求头，用于伪装客户端浏览器，可由抓包获取
header_base = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "cache-control":"no-cache",
    "Connection":"keep-alive",
    "Cookie":"aliyungf_tc=AQAAAMqWGwyUWwIAONRJ3+XkuY/cj6f2; xq_a_token=dac65245b3a3efae1b7df05a0da1e391a1dc9135; xq_a_token.sig=2jFI2opILtFxo21yBLvZ2SnDNZA; xq_r_token=24a12835d176d574c10d976cfc672b9a9d73eba7; xq_r_token.sig=uCuclRLKQMgHs7hWYxhcbMUHu-s; _ga=GA1.2.1953178944.1548052299; _gid=GA1.2.812556881.1548052299; u=311548052299409; Hm_lvt_1db88642e346389874251b5a1eded6e3=1548052300; device_id=eeab31c5d9c7b81e0f38abbd662fcf44; s=fc12m4eok9; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1548138193",
    "Host":"xueqiu.com",
    "Referer":"https://xueqiu.com/hq",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
    }

# 遍历3个链接
for url_url in url:
    response = requests.get(url_url, headers=header_base)
    #转换为dict类型
    res_dict = json.loads(response.text)
    # print(type(res_dict))
    # 获取部分list信
    res_list = res_dict['list']
    # print(type(res_list))
    # 遍历获取的信息
    for res in res_list:
        data = res['data']
        # print(data)
        # 转换为dict类型
        data_dict = json.loads(data)
        # print(type(data_dict))
        # 转换为str类型
        data_id = str(data_dict['id'])
        data_title = str(data_dict['title'])
        data_description = str(data_dict['description'])
        data_target = str(data_dict['target'])
        data = ('用户id:' + data_id, '标题：' + data_title, '描述：' + data_description,'目标：' + data_target)

        print(data)
