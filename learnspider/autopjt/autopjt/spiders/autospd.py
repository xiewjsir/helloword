# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = "autospd"
    allowed_domains = ["sz.lianjia.com"]
    start_urls = (
        'https://sz.lianjia.com/ershoufang/',
    )

    def parse(self, response):
        item = AutopjtItem()

        ulbox = response.xpath("//ul[@class='sellListContent']/li/text()").extract()
        print(ulbox)
        for libox in ulbox:
            # 通过各Xpath表达式分别提取商品的名称、价格、链接、评论数等信息
            item["name"] = libox.xpath("./div[@class='title']/a/text()").extract()
            item["price"] = libox.xpath("./div[@class='address']/a/text()").extract()
            item["link"] = libox.xpath("./div[@class='flood']/a/text()").extract()
            item["comnum"] = libox.xpath("./div[@class='priceInfo']/div[@class='unitPrice']/span/text()").extract()
            # 提取完后返回item
            yield item

        # 接下来很关键，通过循环自动爬取75页的数据
        for i in range(1, 76):
            # 通过上面总结的网址格式构造要爬取的网址
            url = "https://sz.lianjia.com/ershoufang/pg" + str(i) + "/"
            # 通过yield返回Request，并指定要爬取的网址和回调函数
            # 实现自动爬取
            yield Request(url, callback=self.parse)