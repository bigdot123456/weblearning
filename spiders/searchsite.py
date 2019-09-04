# -*- coding: utf-8 -*-
import scrapy


class SearchsiteSpider(scrapy.Spider):
    name = 'searchsite'
    allowed_domains = ['www.1ppt.com/kejian']
    start_urls = ['http://www.1ppt.com/kejian/16501.html']

    def parse(self, response):
        with open("smart.txt",'wb') as f:
            # output = str(response.body, 'utf-8')
            # output = str(response.body)
            output = response.body

            f.write(output)
