import scrapy


class YoukuBasicSpider(scrapy.Spider):
    name = 'youku_basic'
    allowed_domains = ['www.youku.com']
    start_urls = ['http://www.youku.com/']

    def parse(self, response):
        pass
