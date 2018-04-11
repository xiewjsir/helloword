# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import pymongo


class MongoPipeline(object):
    """
    collection = 'lianjia_test'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        table = self.db[self.collection]
        data = dict(item)
        table.insert_one(data)
        return item
"""
    def process_item(self, item, spider):
        print(item)
        """
        {'area': '117.11平米',
         'build_year': '2008年建塔楼',
         'decoration': ' 其他\xa0',
         'elevator': ' 有电梯',
         'floor': '高楼层(共18层)',
         'href': 'https://nj.lianjia.com/chengjiao/NJGL85905392.html',
         'name': '天水滨江花园西苑',
         'orientation': '南 ',
         'region': '鼓楼',
         'sign_time': '2013.09.19',
         'style': '3室2厅',
         'total_price': '365',
         'unit_price': '31168'}        
        """
        return item