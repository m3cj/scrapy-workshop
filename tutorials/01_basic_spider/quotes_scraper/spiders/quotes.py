import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        title = response.css('div.col-md-8 h1 a::text').get()
        
        yield {'title' : title}
