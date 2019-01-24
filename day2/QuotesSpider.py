#coding=utf-8

'''
Created on 2019年1月20日

@author: QINGYUAN
'''
import scrapy
class QuotesSpider(scrapy.Spider):
    '''
    classdocs
    '''
    name = "quotes"
    def start_requests(self):
        urls = [
            'https://xueqiu.com/hq/',
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            ]
        for url in urls:
            print(url)
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self,response):
        page = response.url.split("/")[-2]
        print(page)
        filename = 'quotes-%s.html' % page
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('Save file %s' % filename)
        