import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class VtubersCrawlSpider(CrawlSpider):
    name = "vtubers_crawl"
    allowed_domains = ["vtuber-post.com"]
    start_urls = ["https://vtuber-post.com/database_group.html"]

    rules = [
        Rule(LinkExtractor(restrict_xpaths='//div[@class="clearfix"]/p[@class="name"]/@href'), callback="parse_item", follow=False),
        Rule(LinkExtractor(restrict_xpaths='//p[@class="pagenation bottom"]/a[not(contains(text(),">>")) and contains(text(),">")]/@href'))
    ]

    def parse_item(self, response):
        office_info = response.xpath('//div[@class="data"]')
        yield {
            'officename': office_info.xpath('.//h1[@class="name"]/text()').get(),
            'channel': office_info.xpath('.//p[@class="channel"]/text()').get(),
            'website': office_info.xpath('.//p[@class="website"]/text()').get(),
            'X': office_info.xpath('.//p[contains(text().get(),"X：")]/a/@href').get(),
            'regist': office_info.xpath('.//p[@class="regist"]/text()').get(),
            'play': office_info.xpath('.//p[@class="play"]/text()').get(),
            'upload': office_info.xpath('.//p[@class="upload"]/text()').get(),
            'num': response.xpath('//div[@class="wide database"]/h2/text()').get(),
        }
