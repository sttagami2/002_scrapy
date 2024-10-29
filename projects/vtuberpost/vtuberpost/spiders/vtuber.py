import scrapy


class VtuberSpider(scrapy.Spider):
    name = "vtuber"
    allowed_domains = ["vtuber-post.com"]
    start_urls = ["https://vtuber-post.com/database_group.html"]

    def parse(self, response):
        pass
