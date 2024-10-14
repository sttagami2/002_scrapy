import scrapy


class BooksBasicSpider(scrapy.Spider):
    name = "books_basic"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"]

    def parse(self, response):
        books = response.xpath('//article[contains(@class, "product_pod")]/h3')

        for book in books:
            yield {
                'title': book.xpath('.//a/text()').get(),
                'url': book.xpath('.//a/@href').get()
            }
        
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        # next_pageに値がある場合処理
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
