import scrapy
from ..items import QuotesItem 


class quotesSpider(scrapy.Spider):
    name = 'quotes_css'
    page_no = 2
    start_urls = [
        # 'https://www.goodreads.com/quotes'
        'https://www.goodreads.com/quotes?page=1'
        # 'https://quotes.toscrape.com/'

    ]


    def parse(self, response):

        items = QuotesItem()
        all_quotes = response.css("div.quoteDetails")
        for quote_item in all_quotes:
            quote = quote_item.css('div.quoteText::text').get()
            author = quote_item.css('.authorOrTitle::text').get()
            tags = quote_item.css('.greyText a::text').extract()

            items['quote'] = quote.strip()
            items['author'] = author.strip()
            items['tags'] = tags

            yield items

        
        next_btn = "https://www.goodreads.com/quotes?page="+str(quotesSpider.page_no)

        if quotesSpider.page_no <10 :
            quotesSpider.page_no += 1
            
            yield response.follow(next_btn, callback=self.parse)

        # next_btn = response.css("a.next_page::attr(href)").get()

        # if next_btn != None:
        #     yield response.follow(next_btn, callback=self.parse)