# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeblearningItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    linkurl = scrapy.Field()
    linktxt =scrapy.Field()
    linkdownload = scrapy.Field()
    linkdownname = scrapy.Field()