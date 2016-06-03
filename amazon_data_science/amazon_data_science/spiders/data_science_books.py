# -*- coding: utf-8 -*-
import scrapy
from amazon_data_science.items import AmazonDataScienceItem

class DataScienceBooksSpider(scrapy.Spider):
    name = "data_science_books"
    allowed_domains = ["amazon.com"]
    start_urls = (
        'http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=data+science+books',
    )

    def build_item(self, book):
        title_date_author = book.xpath("descendant::div[@class='a-row a-spacing-small']")
        title = title_date_author.xpath("a/h2/text()")[0]
        date = title_date_author.xpath("span[@class='a-size-small a-color-secondary']/text()")[0]
        author = title_date_author.xpath("div[@class='a-row a-spacing-none']/descendant::*/text()")[1:]

        item = AmazonDataScienceItem()
        item['title'] = title.extract()
        item['date'] = date.extract()
        item['author'] = " ".join(author.extract())
        return item

    def parse(self, response):
        books = response.xpath("//div[@class='s-item-container']")
        for book in books:
            yield self.build_item(book)

        next_link = response.xpath("//a[@id='pagnNextLink']/@href").extract()
        if next_link:
            url = response.urljoin(next_link[0])
            # uncomment this line to keep on scraping next pages
            # yield scrapy.Request(url, self.parse)
