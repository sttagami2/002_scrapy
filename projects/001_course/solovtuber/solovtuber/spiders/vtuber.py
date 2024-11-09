import scrapy


class VtuberSpider(scrapy.Spider):
    name = "vtuber"
    allowed_domains = ["note.com"]
    start_urls = ["https://note.com/virtualinlimbo/n/n48a4b96ade8e"]

    def parse(self, response):
        names = response.xpath('//div[@class="note-common-styles__textnote-body"]/p/text()').getall()
        xurls = response.xpath('//div[@class="note-common-styles__textnote-body"]/p/a/@href').getall()
        # yield：関数の処理を一旦停止し値を返す
        yield {
            'name': names,
            'xurl': xurls
        }
