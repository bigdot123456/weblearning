# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

import items
import requests
import DownloadURL

class SearchsiteSpider(scrapy.Spider):
    name = 'searchsite'
    # allowed_domains = ['www.1ppt.com/kejian']
    start_urls = 'http://www.1ppt.com/kejian/shuxue/293/'
    header = 'http://www.1ppt.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = self.start_urls
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = items.WeblearningItem()
        # /// div / ul / li[9] / a
        # / html / body / div[5] / div[1] / dl / dd / div / ul / li[9] / a
        # nextpage = response.xpath('//div/ul/li[9]/a/@ref').extract()

        # response.xpath('//a[contains(@href,“下一页”)]/@href')
        ## 获得下一页整个的内容，可以直接打开，html文件，然后利用查找，根据dom结构，找到类名称为ul class="pages"
        # response.xpath('//ul[@class="pages"]').extract()
        ## 直接通过查找法，获得 下一页 标签内容
        response.xpath('//a[contains(text(), "下一页")]')
        ## 直接通过查找法，获得标签内容的超链接,如果有多个，建议直接下载
        response.xpath('//a[contains(text(), "下一页")]/@href')
        # // a[contains(text(), "百度搜索")]

        # htmllist=response.xpath('/html/body/div[5]/div[1]/dl/dd/ul/li')
        # 获得超链接文本
        txt = response.xpath('//ul[@class="arclist"]/li/h2/a/text()').extract()
        # 获得超链接地址
        links = response.xpath('//ul[@class="arclist"]/li/h2/a/@href').extract()

        with open("smart.txt", 'wb') as f:
            # output = str(response.body, 'utf-8')
            # output = str(response.body)
            output = response.body

            f.write(output)

        next_url = response.xpath('//a[contains(text(), "下一页")]/@href').extract()
        if next_url:
            nextpage = f"{self.start_urls}{next_url[0]}"
            # print(f"debug:  ${nextpage}")
            yield Request(nextpage, headers=self.headers)

        i = 0
        for link in links:
            linkurl = f"{self.header}{link}"
            item['linkurl'] = linkurl
            item['linktxt'] = txt[i]
            i = i + 1
            yield scrapy.Request(url=linkurl, meta={'item': item}, callback=self.parse_sub, dont_filter=True)
            # yield item

    def parse_sub(self, response):
        # 传递参数
        item = response.meta['item']
        linkdownname = response.xpath('//head/meta[3]/@content')[0].extract()
        linkfilename = linkdownname.replace(',', '_')
        linkurl = response.xpath('//ul[@class="downurllist"]//a/@href')[0].extract()

        item['linkdownname'] = linkfilename
        item['linkdownload'] = linkurl
        yield item

        # resource = requests.get(linkurl, stream=True)
        # print(f"Downloading {linkfilename} with {linkurl}")
        # with open(linkfilename, mode="wb") as fh:
        #     for chunk in resource.iter_content(chunk_size=2048):
        #         fh.write(chunk)
        DownloadURL.DownloadURL(linkurl,f"Download/{linkfilename}.rar")
        # print(f"data:{item}")
