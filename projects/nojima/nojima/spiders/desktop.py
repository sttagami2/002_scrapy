import scrapy


class DesktopSpider(scrapy.Spider):
    name = "desktop"
    allowed_domains = ["online.nojima.co.jp"]
    start_urls = ["https://online.nojima.co.jp/category/10003251"]

    def parse(self, response):
        pass
