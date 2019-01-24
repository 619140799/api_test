# -*- coding: utf-8 -*-

#导入requests包
import requests
#导入json包
import json

import urllib
import urllib3
'''
#========================
#一个最简单的get请求
#========================

#1.组装请求
url = "http://httpbin.org/get" # 这里只有url,字符串格式
# 2.发送请求，获取响应
res = requests.get(url) #res即返回的响应对象
# 3.解析响应
print(res.text) #输出响应的文本


#==================================
#带参数的get请求1
#==================================
url1 = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好" #参数可以写到URL里

res1 = requests.get(url=url1) #第一个url指get方法的参数，第二个url指上一行我们定义的接口地址

print(res1.text)

#==================================
#带参数的get请求2
#==================================
url2 = "http://www.tuling123.com/openapi/api"
params = {"key":"ec961279f453459b9248f0aeb6600bbe","info":"你好"} #字典格式，单独提出来，方便参数的添加修改等操作
res2 = requests.get(url=url2, params=params)
print(res2.text)

#=====================================
#传统表单类post请求（x-www-form-urlencoded）
#=====================================

posturl = "http://httpbin.org/post" 
data = {"name":"hanzhichao","age":18} #post请求发送的数据，字典格式
postres = requests.post(url=posturl,data=data) #这里使用post方法，参数和get方法一样
print(postres.text)
'''
'''
#=====================================
#传统表单类post请求（x-www-form-urlencoded）
#=====================================
posturl = "http://httpbin.org/post" 
data = '{
    "name":"hanzhichao",
    "age":18
    } ' #多行文本，字符串格式，也可以单行（注意外层有引号，为字符串）data = '{"name":"hanzhichao","age":18}
postres = requests.post(url=posturl,data=data) #data支持字典或字符串
print(postres.text)



#====================================
#使用json格式化数据
#====================================
url = "http://httpbin.org/post"
data = {
        "name":"hanzhichao",
        "age":18} #字典格式，方便添加
headers = {"Content-Type":"application/json"} #严格来说，我们需要在请求头里声明我们发送的的格式
res = requests.post(url=url,data=json.dumps(data),headers=headers) #将字典格式的data变量转换为合法的JSON字符串传给Post的data参数
print(res.text)


#====================================
#使用post方法的Json参数
#====================================
url = "http://openapi.tuling123.com/openapi/api/v2"
data = {
    "reqType":0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "北京",
                "street": "信息路"
            }
        }
    },
    "userInfo": {
        "apiKey": "ec961279f453459b9248f0aeb6600bbe",
        "userId": "206379"
    }
} #字典格式，方便添加
res = requests.post(url=url,json=data) #json格式的请求，将数据赋给json参数
print(res.text)

#=======================================
#文件的序列化与反序列化
#序列化：字典-》文件句柄
#=======================================
res_dict = {"name":"张三","password":"123456","male":True,"money":None} #字典格式
f = open("demo1.json","w")
json.dump(res_dict, f)

print(f)


#=======================================
#文件的序列化与反序列化
#序列化：文件句柄->字典
#=======================================

f = open("demo2.json", "r", encoding="utf-8") #文件中有中文需要指定编码
f_dict1 = json.load(f) #反序列化将文件句柄转化为字典
print(f_dict1['name']) #读取其中参数
print(f_dict1)
f.close()



#==========================================
#解析demo3文件并发送请求并响应
#注： method支持get和post，如果没有method，有data默认发post请求，没有data默认发get请求，type支持：form或json，没有默认发form格式
#==========================================

#打开demo3.json文件，并指定编码
f = open("demo3.json", "r", encoding="utf-8")
res = json.load(f)
print(res['method'])
s = requests.request(res['method'],url=res['url'],params=res['params'])
print(s.status_code)
print(s.text)
f.close()

'''

url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
cookies = {"PHPSESSID":"5e271db9d611bd4461becf167585677c"}

res = requests.get(url=url, cookies=cookies)
print(res.text)

#=========================================================================
#调用百度AI图片识别接口进行识别图片中的文字
#
#
#=========================================================================

app_key = 'W9M51D0iNGetUiu7CXL4S1Ey'
secret_key = '2hYzsZNTn2Os4M1VS4bNPrjXlOOGq3G5'
img_url = 'http://upload-images.jianshu.io/upload_images/7575721-40c847532432e852.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
# 获取token
get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(app_key,secret_key)
token = requests.get(url=get_token_url).json().get("access_token")  # 从获取token接口的响应中取得token值
print(token)
# 识别图片文字
orc_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}'.format(token)
data = {"url": img_url}
res = requests.post(url=orc_url, data=data)
print(json.dumps(res.json(), indent=2, ensure_ascii=False)) # 格式化输出





'''
人脸检测与属性分析
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"


params = "{\"image\":\"027d8308a2ec665acb1bdf63e513bcb9\",\"image_type\":\"FACE_TOKEN\",\"face_field\":\"faceshape,facetype\"}"

access_token = '24.c08c7ea0f7e1ded70569cb5b809f43a1.2592000.1549701157.282335-15391346'
request_url = request_url + "?access_token=" + access_token
request = urllib3.request(url=request_url, data=params)
request.add_header('Content-Type', 'application/json')
#response = urllib3.urlopen(request)
response = urllib3.connection_from_url(request)
content = response.read()
if content:
    print(content)
