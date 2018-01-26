# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class DoubanMovieItem(Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	ranking = Field()
	movie_name = Field()
	score = Field()
	score_num = Field()

class ZufangItem(Item):
    title = Field()
    link = Field()
    time = Field()
    commentCount = Field()#计划改进有效评论数

class ZufangContentItem(Item):
	contents = Field()
	fromUser = Field()
	userLink = Field()
	detailTime = Field()
	linkId = Field()