import scrapy


class QuotesSpider(scrapy.Spider):
    name = "youku"

    def start_requests(self):
        urls = [
            'https://list.youku.com/category/show/c_97.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('ul.panel > li > div.yk-pack'):
            yield {
                'title': quote.css('ul > li.title > a::text').get(),
                'itemLink': "http:"+quote.css('ul > li.title > a::attr(href)').get(),
            }
