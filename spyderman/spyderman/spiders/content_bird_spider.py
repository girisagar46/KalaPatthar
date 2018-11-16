# -*- coding: utf-8 -*-
import json
from uuid import uuid4

import scrapy
from django.db import transaction
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from core.models import (BlogData, Website)

filename = "book_titles.txt"


class ContentBirdSpider(CrawlSpider):

    name = 'content_bird_spider'

    allowed_domains = ['de.contentbird.io']

    start_urls = ['https://de.contentbird.io/blog/']

    rules = (Rule(LinkExtractor(allow=('page')), callback="parse"), )


    def parse(self, response):
        links = response.xpath('//*[@id="content"]/div/section/header/h2/a/@href').extract()
        paginations = response.xpath('//*[@id="nav-below"]/div/a/@href').extract()

        for link in links[:1]:
            yield scrapy.Request(url=link, callback=self.process)

        # for pag in paginations[:2]:
        #     yield scrapy.Request(url=pag, callback=self.parse)

    def process(self, response):
        title = response.xpath('//*[@id="content"]/article/header/h1/text()').extract()
        body = response.xpath('//*[@class="post-content"]//h2/following-sibling::*[self::h3 '
                              'or self::p or self::a]//text()').extract()
        images_src = response.xpath('//*[@id="content"]/article/div//img/@src').extract()
        anchor_links = response.xpath('//*[@id="content"]/article/div//a/@href').extract()
        anchor_text = response.xpath('//*[@id="content"]/article/div//a/text()').extract()

        web = Website()
        web.website_name=response.url
        web.title=" ".join(title).strip()
        web.save()

        if web:
            blog_data = BlogData()
            blog_data.unique_id=str(uuid4())
            blog_data.website=web
            blog_data.body=json.dumps(body)
            blog_data.images_srcs=json.dumps(images_src)
            blog_data.anchor_links=json.dumps(anchor_links)
            blog_data.anchor_texts=json.dumps(anchor_text)
            blog_data.save()