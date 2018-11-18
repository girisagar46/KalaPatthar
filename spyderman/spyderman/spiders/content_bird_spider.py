# -*- coding: utf-8 -*-
import json
from uuid import uuid4

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from core.models import (BlogData, Website)

class ContentBirdSpider(CrawlSpider):

    name = 'content_bird_spider'

    allowed_domains = ['de.contentbird.io']

    start_urls = ['https://de.contentbird.io/blog/']

    rules = (Rule(LinkExtractor(allow=('page')), callback="parse"), )

    def parse(self, response):
        # Extract all links form the first page which is in the start_urls list
        links = response.xpath('//*[@id="content"]/div/section/header/h2/a/@href').extract()

        # Since, posts are paginated, find the pagination link in each blog post
        paginations = response.xpath('//*[@id="nav-below"]/div/a/@href').extract()

        for link in links:
            # yield the request object which calls process function that processes the file and adds to db
            yield scrapy.Request(url=link, callback=self.process)

        for pag in paginations:
            # each pagination call parse function recursively so that all blog pages are traversed
            yield scrapy.Request(url=pag, callback=self.parse)

    def process(self, response):
        title = response.xpath('//*[@id="content"]/article/header/h1/text()').extract()
        body = response.xpath('//*[@class="post-content"]//h2/following-sibling::*[self::h3 '
                              'or self::p or self::a]//text()').extract()
        images_src = response.xpath('//*[@id="content"]/article/div//img/@src').extract()
        anchor_links = response.xpath('//*[@id="content"]/article/div//a/@href').extract()
        anchor_text = response.xpath('//*[@id="content"]/article/div//a/text()').extract()

        web = Website()
        web.website_name = response.url
        web.title = " ".join(title).strip()
        web.save()

        if web:
            blog_data = BlogData()
            blog_data.unique_id = str(uuid4())
            blog_data.website = web
            blog_data.body = json.dumps(body)
            blog_data.images_srcs = json.dumps(images_src)
            blog_data.anchor_links = json.dumps(anchor_links)
            blog_data.anchor_texts = json.dumps(anchor_text)
            blog_data.save()