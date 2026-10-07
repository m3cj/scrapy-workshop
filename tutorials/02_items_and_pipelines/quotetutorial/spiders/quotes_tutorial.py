import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]
    
    def parse(self, response):
        all_div = response.css('div.quote')
        
        items = QuotetutorialItem()
        
        for quote in all_div:
            title = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tags = quote.css('a.tag::text').extract()
            
            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            
            yield items