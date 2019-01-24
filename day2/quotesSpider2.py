#coding=utf-8
'''
Created on 2019年1月21日

@author: QINGYUAN
'''
import scrapy

class QuoutesSpider2(scrapy.Spider):
    '''
    classdocs
    '''
    name = "quotes2"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        ]
    def parse(self,response):
        for quote in response.css('div.quote'):
            yield{
                'text':quote.css('span.text::text').extract_first(),
                'author':quote.css('small.author::text').extract_first(),
                'tags':quote.css('div.tags a.tag::text').extract()
                }

