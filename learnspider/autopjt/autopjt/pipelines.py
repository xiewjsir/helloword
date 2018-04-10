# -*- coding: utf-8 -*-
import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutopjtPipeline(object):
    def __init__(self):
        # 打开mydata.json文件
        self.file = codecs.open("D:/www/learn-python/learnspider/mydata.json", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        i = json.dumps(dict(item), ensure_ascii=False)
        # 每条数据后加上换行
        line = i + '\n'
        print(line)
        # 写入数据到mydata.json文件中
        #self.file.write(line)
        return item

    def close_spider(self, spider):
        # 关闭mydata.json文件
        self.file.close()
