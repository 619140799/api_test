#coding=utf-8
'''
Created on 2019年1月21日

@author: QINGYUAN
'''
import scrapy

class XueQiuSpider(scrapy.Spider):
    '''
    classdocs
    '''
    name = "xueqiu"
    start_urls = [
        'https://xueqiu.com/hq'
        ]
    def parse(self,response):
        for quote in response.xpath('//div[@class="stock-preview module-container"]/div[@class="detail-container new-portfolio"]/table[@class="portfolio"]'):
            
            yield{
                'titlename':quote.xpath('.//thead[1]/tr[1]/th[1]/text()').extract()
                }




