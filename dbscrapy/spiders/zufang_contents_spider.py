# coding=UTF-8
from scrapy.spiders import Spider
from dbscrapy.items import ZufangContentItem
from scrapy import Request
from dbscrapy.sqlUtil import sqlUtil
import json

#租房详细信息爬虫
class ZufangContentsSpider(Spider):
    name = 'ZufangContentsSpider'
#请求头部
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
#初始请求URL
    util = sqlUtil()
    data = util.queryBySql("SELECT id, link from zufang")
    urls = util.dealWithLinkList(data)
    url = ['https://www.douban.com/group/topic/108727990/']
    print (data)
    start_urls = urls

    def start_requests(self):
        util = sqlUtil()
        data = util.queryBySql("SELECT id, link from zufang")
        urls = util.dealWithLinkList(data)
        # url = ['https://www.douban.com/group/topic/108727990/']
        # print (urls)
        for url in urls:
            yield Request(url.get('link') ,meta={'urlid':url.get('id')}, headers=self.headers)

    # def start_requests(self):
    #     url = 'https://www.douban.com/group/topic/112166728/'
    #     yield Request(url, headers=self.headers)

    def parse(self, response):
        item = ZufangContentItem()
        contents = response.xpath('//div[@class="topic-doc"]')
        for content in contents:

            # 判空处理
            mylist = content.xpath(
                './/div[@id="link-report"]/div[@class="topic-content"]/.')#text() 取不到换成’.‘ --- 参见xpath中text()和‘.’和string()的区别
            if mylist:

                imgList = mylist.xpath('.//div[@class="image-wrapper"]/img/@src')
                mylist = mylist.xpath('string(.//p)') #string 的用法
                dic={'contents':mylist.extract()[0].replace('\n', ''),'img':"<link>".join(imgList.extract())}
                item['contents'] = json.dumps(dic,ensure_ascii=False)#禁用ascii编码 防止中文乱码

            mylist = content.xpath(
                './/h3/span[@class="from"]/a/text()')
            if mylist:
                item['fromUser'] = mylist.extract()[0]


            mylist = content.xpath(
                './/h3/span[@class="from"]/a/@href')
            if mylist:
                item['userLink'] = mylist.extract()[0]

            mylist = content.xpath(
                './/h3/span[@class="color-green"]/text()')
            if mylist:
                item['detailTime'] = mylist.extract()[0]

            item['linkId'] = str(response.meta['urlid'])

            yield item

            #下一页链接
            # next_url = response.xpath('//span[@class="next"]/a/@href').extract()
            # next_url = next_url[0]
            # yield Request(next_url, headers=self.headers)

    def formatList(self,aList):
        result = ""
        for str in aList:
            result = result,"",str
            return result