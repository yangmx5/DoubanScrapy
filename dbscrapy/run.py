# -*- coding: utf-8 -*-
from scrapy import  cmdline

# name = 'ZufangContentsSpider'

name = 'ZufangSpider'

#限制爬虫抓取URL 深度  并输出至csv文件
# cmd = 'scrapy crawl {0} -s CLOSESPIDER_PAGECOUNT=2 -o ../../zuFang.csv'.format(name)
cmd = 'scrapy crawl {0} -s CLOSESPIDER_PAGECOUNT=2 -o ./zuFang.csv'.format(name)
# cmd = 'scrapy crawl {0} -o ../../zuFang.csv'.format(name) #由于设置了CLOSESPIDER_PAGECOUNT 所以start urls 中的链接不能全部被爬取完
cmdline.execute(cmd.split())