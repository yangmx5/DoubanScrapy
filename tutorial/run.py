# -*- coding: utf-8 -*-
from scrapy import  cmdline

name = 'ZufangSpider'
cmd = 'scrapy crawl {0} -s CLOSESPIDER_PAGECOUNT=5 -o zuFang.csv'.format(name)
cmdline.execute(cmd.split())