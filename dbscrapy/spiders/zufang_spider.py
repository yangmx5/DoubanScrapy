# coding=UTF-8
from scrapy.spiders import Spider
from dbscrapy.items import ZufangItem
from scrapy import Request

#租房爬虫
class ZufangSpider(Spider):
    name = 'ZufangSpider'
#请求头部
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, 			like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
#初始请求URL
    def start_requests(self):
        url = 'https://www.douban.com/group/beijingzufang/discussion'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = ZufangItem()
        contents = response.xpath('//table[@class="olt"]/tr')
        for content in contents:

            # 判空处理
            mylist = content.xpath(
                './/td[@class="title"]/a/text()')
            if mylist:
                item['title'] = mylist.extract()[0].strip() #添加去空格函数


            mylist = content.xpath(
                './/td[@class="title"]/a/@href')
            if mylist:
                item['link'] = mylist.extract()[0]


            mylist = content.xpath(
                './/td[@class="time"]/text()')
            if mylist:
                item['time'] = mylist.extract()[0]

            mylist = content.xpath(
                './/td[@class=""]/text()')
            if mylist:
                item['commentCount'] = mylist.extract()[0]

            yield item

            #下一页链接
            next_url = response.xpath('//span[@class="next"]/a/@href').extract()
            next_url = next_url[0]
            yield Request(next_url, headers=self.headers)
