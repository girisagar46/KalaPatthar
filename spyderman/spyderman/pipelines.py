# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from core.models import (Website, BlogData)

class SpydermanPipeline(object):

    def __init__(self, unique_id, website_name, *args, **kwargs):
        self.unique_id = unique_id
        self.website_name = website_name
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
            website_name=crawler.settings.get('website_name'),
        )

    def close_spider(self, spider):
        website = Website.objects.create(self.website_name)

        # website_data = WebsiteData()
        # unique_id =
        # website =
        # title =
        # body =
        # images_src =
        # anchor_links =
        # anchor_text =
        # item.unique_id = self.unique_id
        # item.data = json.dumps(self.items)
        # item.save()

    def process_item(self, item, spider):
        self.website_name.append(item['url'])
        return item
