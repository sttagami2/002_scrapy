import scrapy


class DesktopSpider(scrapy.Spider):
    name = "desktop"
    allowed_domains = ["www.yodobashi.com"]
    start_urls = ["https://www.yodobashi.com/category/19531/500000117014/500000116005"]

    def parse(self, response):
        # 商品取得
        products = response.xpath('//div[contains(@class,"productListTile")]')
        # products = response.css('div.productListTile')
        for product in products:
            # メーカー名
            # 一度取得したproductsのデータを扱うので、「.」を使う必要がある
            maker = product.xpath('.//div[contains(@class,"pName")]/p/text()').get()
            # maker = product.css('div.pName > p::text')

            # 商品名
            name = product.xpath('.//div[contains(@class,"pName")]/p[2]/text()').get()

            # 価格
            price = product.xpath('.//span[@class="productPrice"]/text()').get()

            yield {
                'maker': maker,
                'name': name,
                'price': price
            }
