# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class BotcnblogsPipeline(object):
    def __init__(self):
        self.file = open("item.json", "w+")

    def process_item(self, item, spider):
        record = json.dumps(dict(item), ensure_ascii=False)+"\n"
        self.file.write(record)
        return item
