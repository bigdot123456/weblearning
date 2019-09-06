#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.cmdline import execute

if __name__ == "__main__":
    execute(["scrapy", "crawl", "searchsite", "-o", "item.json"])
