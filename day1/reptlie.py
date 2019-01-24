#coding:utf-8
from urllib import request
'''
爬虫demo
'''
#===============================
#爬虫V1.0 利用urllib和字符串内建函数
#===============================

def getHtml(url):
    #获取网页内容
    print("爬取网页")
    page = request.urlopen(url)
    html = page.read()
    html1 = html.decode("UTF-8")
    print('返回网页内容')
    print(html1)
    '''
    for i in range(len(html)):
        print(i)'''
    return html1
    
def content(html):
    #内容分割的标签
    str = '<header class="article-header">'
    str = bytes(str,encoding="utf-8")
    print(str)
    print(html.findall(str))
    content = html.partition(str)[2]
    print(content)
    str1 = ''
    content = content.partition(str1)[0]
    return content #得到网页的内容

def title(content,beg = 0):
    #匹配title
    #思路是利用str.index()和序列的切片
    try:
        title_list = []
        while True:
            num1 = content.index('】',beg)+3
            num2 = content.index('</p>',num1)
            title_list.append(content[num1:num2])
            beg = num2
    except ValueError:
        return title_list

def get_img(content,beg=0):
    #匹配图片的url
    #思路是利用str.index()和序列的切片
    try:
        img_list = []
        while True:
            src1 = content.index('http',beg)
            src2 = content.index('/></p>',src1)
            img_list.append(content[src1:src2])
            beg =src2
    except ValueError:
        return img_list
    
def many_img(data,beg = 0):
    #用于匹配多图中的url
    try:
        many_img_str = ''
        while True:
            src1 = data.index('http',beg)
            src2 = data.index(' /><br /><img src=',src1)
            many_img_str += data[src1:src2]+'|' #多个图片的url用“|”隔开
            beg = src2
    except ValueError:
        return many_img_str
    
def data_out(title,img):
    #写入文本
    with open("/yangqing/data.txt", "a+") as fo:
        fo.write('\n')
        for size in range(0,len(title)):
            #判断img[size]中存在的是不是一个url
            if len(img[size]) > 70:
                img[size] = many_img(img[size]) #调用many_img()方法
            fo.write(title[size]+'$'+img[size]+'\n')
            
            
            
content = content(getHtml("https://bh.sb/post/41703/"))
title = title(content)
img = get_img(content)
data_out(title, img)