# -*- coding: utf-8 -*-
import scrapy
import items
class SearchsiteSpider(scrapy.Spider):
    name = 'searchsite'
    allowed_domains = ['www.1ppt.com/kejian']
    start_urls = ['http://www.1ppt.com/kejian/shuxue/293/']
    header='http://www.1ppt.com'

    def parse(self, response):
        item=items.WeblearningItem()

        #htmllist=response.xpath('/html/body/div[5]/div[1]/dl/dd/ul/li')
        # 获得超链接文本
        txt=response.xpath('//ul[@class="arclist"]/li/h2/a/text()').extract()
        # 获得超链接地址
        links=response.xpath('//ul[@class="arclist"]/li/h2/a/@href').extract()

        i=0
        for link in links:
            item['linkurl']=f"{self.header}{link}"
            item['linktxt']=txt[i]
            i=i+1
            yield item

        with open("smart.txt",'wb') as f:
            # output = str(response.body, 'utf-8')
            # output = str(response.body)
            output = response.body

            f.write(output)
