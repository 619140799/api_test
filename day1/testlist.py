# -*- coding: utf-8 -*-

'''
Created on 2019��1��7��

@author: QINGYUAN
'''
import urllib3
import urllib
from types import *
import hashlib
from pip._internal import req


import requests
###列表
squares = [1,5,0,9,5,7,0]

print(squares)


print(squares[0])

print(squares[-1])

print(squares[-3:])

print(squares[:])

print(squares + [11,34,10,33])


cubes = [1,33,5,10,98]

print(4 ** 3)

cubes[3] = 64

print(cubes)




def synmackey():
    url = 'http://20.0.1.157:30043/ABS'
    headers = {'uid':'ABS','flag':'L',}
    response = requests.post(url,headers=headers)
    
    head = response.headers
    print(head)
    
    x = requests.structures.CaseInsensitiveDict(head)
    
    js = dict(x)
    
    js.get('mackey')



