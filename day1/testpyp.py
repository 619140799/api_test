#coding=utf-8

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
from pandas import DataFrame 

class DoctorSpider(object):
    def __init__(self):
        self._data = list()
        
    async def main(self,num):
        try:
            browser = await launch(headless=True)
            page = await browser.newPage()
            print(f"正在爬取第{num}页面")
            await page.goto("https://www.guahao.com/expert/all/全国/all/不限/p{}".format(num))
            content = await page.content()
            
            self.parse_html(content)
            print("正在存储数据。。。。")
            
            data = DataFrame(self._data)
            
            data.to_csv("微医数据.csv",encoding='utf_8_sig')
            
        except Exception as e:
            print(e.args)
        finally:
            num+=1
            await browser.close()
            await self.main(num)


    def parse_html(self,content):
        doc = pq(content)
        items = doc(".g-doctor-item").items()
        for item in items:
            name_level = item.find(".g-doc-baseinfo>dl>dt").text() #姓名和级别
            department = item.find(".g-doc-baseinfo>dl>dd>p:eq(0)").text() #科室
            address = item.find(".g-doc-baseinfo>dl>dd>p:eq(1)").text() #医院地址
            star = item.find(".star-count em").text() #评分
            inquisition = item.find(".star-count i").text() #问诊量
            expert_team = item.find(".expert-team").text() #专家团队
            service_price_img = item.find(".service-name:eq(0)>.fee").text()
            service_price_video = item.find(".service-name:eq(1)>.fee").text()
            
            one_data = {
                "name":name_level.split(" ")[0],
                "level":name_level.split(" ")[1],
                "department":department,
                "address":address,
                "star":star,
                "inquisition":inquisition,
                "expert_team":expert_team,
                "service_price_img":service_price_img,
                "service_price_video":service_price_video}
            
            self._data.append(one_data)
            
    def run(self):
        loop = asyncio.get_event_loop()
        asyncio.get_event_loop().run_until_complete(self.main(1))
        


if __name__ == '__main__':
    doctor = DoctorSpider()
    doctor.run()

'''    
async def main():
    browser = await launch() #运行一个无头的浏览器
    page = await browser.newPage()  #打开一个选项卡
    await page.goto("http://www.baidu.com") #加载一个页面
    await page.screenshot({'path':'baidu.png'}) #把网页生成截图
    await browser.close()
    
asyncio.get_event_loop().run_until_complete(main()) #异步

'''