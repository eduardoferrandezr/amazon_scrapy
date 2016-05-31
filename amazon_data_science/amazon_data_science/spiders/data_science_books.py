# -*- coding: utf-8 -*-
import scrapy


class DataScienceBooksSpider(scrapy.Spider):
    name = "data_science_books"
    allowed_domains = ["amazon.com"]
    start_urls = (
        'http://www.amazon.com/',
    )

    def parse(self, response):
        pass
