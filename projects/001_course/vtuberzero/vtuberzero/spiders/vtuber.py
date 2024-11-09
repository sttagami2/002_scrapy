import scrapy


class VtuberSpider(scrapy.Spider):
    name = "vtuber"
    allowed_domains = ["vtub0.com"]
    start_urls = ["https://vtub0.com/vtuber"]

    def parse(self, response):
        names = response.xpath('//tr/td[2]//a//text()').getall()
        xurls = response.xpath('//tr/td[3]/strong/a[contains(@href,"twitter")][1]/@href').getall()
        yurls = response.xpath('//tr/td[3]/strong/a[contains(@href,"youtube")][1]/@href').getall()
        # yield：関数の処理を一旦停止し値を返す
        yield {
            'name': names,
            'xurl': xurls,
            'yurls': yurls
        }
