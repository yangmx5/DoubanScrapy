# coding=UTF-8
from scrapy.spiders import Spider
from tutorial.items import ZufangItem
from scrapy import Request


class ZufangSpider(Spider):
    name = 'ZufangSpider'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, 			like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://www.douban.com/group/beijingzufang/discussion'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = ZufangItem()
        contents = response.xpath('//table[@class="olt"]/tr')
        for content in contents:

            mylist = content.xpath(
                './/td[@class="title"]/a/text()')
            if mylist:
                item['title'] = mylist.extract()[0]


            mylist = content.xpath(
                './/td[@class="title"]/a/@href')
            if mylist:
                item['link'] = mylist.extract()[0]


            mylist = content.xpath(
                './/td[@class="time"]/text()')
            if mylist:
                item['time'] = mylist.extract()[0]

            yield item

            next_url = response.xpath('//span[@class="next"]/a/@href').extract()
            next_url = next_url[0]
            yield Request(next_url, headers=self.headers)
