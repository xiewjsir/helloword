#��17��Scrapy�߼�Ӧ��
#17.1 Python3��β������ݿ�
#(1)
D:\Python35\myweb\part16\mycwpjt>pip install pymysql3
Collecting pymysql3
  Downloading PyMySQL3-0.5.tar.gz
running egg_info
����
  Stored in directory: C:\Users\Administrator.USER-20160828PN\AppData\Local\pip\Cache\wheels\bf\84\b3\c2cb0d3d8e99f408976e112f65ba4780cbfb446a606dd620db
Successfully built pymysql3
Installing collected packages: pymysql3
Successfully installed pymysql3-0.5

#(2)
>>> cs=conn1.cursor()
>>> cs.execute("select * from mytb")
1
>>> for i in cs:
	print("��ǰ�ǵ�"+str(cs.rownumber)+"��")
	print("�����ǣ�"+i[0])
	print("�ؼ����ǣ�"+i[1])

#17.2 ��ȡ����д��MySQL
#(1)
D:\Python35\myweb\part17>scrapy startproject mysqlpjt
New Scrapy project 'mysqlpjt', using template directory 'd:\\python35\\lib\\site-packages\\scrapy\\templates\\project', created in:
    D:\Python35\myweb\part17\mysqlpjt
You can start your first spider with:
    cd mysqlpjt
    scrapy genspider example example.com

#(2)
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MysqlpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #����name�洢��ҳ����
    name=scrapy.Field()
    #����keywd�洢��ҳ�ؼ���
    keywd=scrapy.Field()

#(3)
# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysqlpjtPipeline(object):
    def __init__(self):
        #�տ�ʼʱ���Ӷ�Ӧ���ݿ�
        self.conn=pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="mypydb")
    def process_item(self, item, spider):
        #����ȡ����name��keywd�ֱ𸳸�����name�ͱ���key
        name=item["name"][0]
        key=item["keywd"][0]
        #�����Ӧ��sql���
        sql="insert into mytb(title,keywd) VALUES('"+name+"','"+key+"')"
        #ͨ��queryʵ��ִ�ж�Ӧ��sql���
        self.conn.query(sql)
        return item
    def close_spider(self,spider):
        self.conn.close()

#(4)
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'mysqlpjt.pipelines.MysqlpjtPipeline': 300,
}

#(5)
D:\Python35\myweb\part17\mysqlpjt>scrapy genspider -t crawl weiwei sina.com.cn
Created spider 'weiwei' using template 'crawl' in module:
  Mysqlpjt.spiders.weiwei

#(6)
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mysqlpjt.items import MysqlpjtItem


class WeiweiSpider(CrawlSpider):
    name = 'weiwei'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/[0-9]{4}.[0-9]{2}.[0-9]{2}.doc-.*?shtml'),allow_domains=('sina.com.cn')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = MysqlpjtItem()
        #ͨ��xpath���ʽ��ȡ��ҳ����
        i["name"]=response.xpath("/html/head/title/text()").extract()
        #ͨ��xpath���ʽ��ȡ��ҳ�Ĺؼ���
        i["keywd"]=response.xpath("/html/head/meta[@name='keywords']/@content").extract()
        return i

#(7)
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#(8
   def __init__(self, host="localhost", user=None, passwd="",
                 db=None, port=3306, unix_socket=None,
                 charset='utf8', sql_mode=None,
                 read_default_file=None, conv=decoders, use_unicode=None,
                 client_flag=0, cursorclass=Cursor, init_command=None,
                 connect_timeout=None, ssl=None, read_default_group=None,
                 compress=None, named_pipe=None):







)
