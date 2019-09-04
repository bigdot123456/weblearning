# -*- coding: utf-8 -*-
import scrapy


class SearchsiteSpider(scrapy.Spider):
    name = 'searchsite'
    allowed_domains = ['http://www.1ppt.com/kejian/16501.html']
    start_urls = ['http://http://www.1ppt.com/kejian/16501.html/']

    def parse(self, response):
        pass
