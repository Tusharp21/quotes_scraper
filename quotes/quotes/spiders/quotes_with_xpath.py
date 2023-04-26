import scrapy
from ..items import QuotesItem 


class quotesSpider(scrapy.Spider):
    name = 'quotes_xpath'
    start_urls = [
        'https://www.goodreads.com/quotes'
        # 'https://quotes.toscrape.com/'

    ]

    def parse(self, response):

        items = QuotesItem()
        all_quotes = response.xpath("//div[@class='quoteDetails']")
        for quote_item in all_quotes:
            quote = quote_item.xpath('//div[@class="quoteText"]/text()').get()
            author = quote_item.xpath('//span[@class="authorOrTitle"]/text()').get()
            tags = quote_item.xpath('//div[@class="greyText"]/a/text()').extract()
            

            items['quote'] = quote.strip()
            items['author'] = author.strip()
            items['tags'] = tags

            yield items

        # all_quotes = response.css("div.quoteDetails")

        
        # for quote_item in all_quotes:
        #     quote = quote_item.css('div.quoteText::text').get()
        #     author = quote_item.css('.authorOrTitle::text').get()
        #     tags = quote_item.css('.greyText a::text').extract()

        #     items['quote'] = quote.strip()
        #     items['author'] = author.strip()
        #     items['tags'] = tags

        #     yield items

        
        # all_quotes = response.css("div.quote")

        
        # for quote_item in all_quotes:
        #     quote = quote_item.css('span.text::text').extract()
        #     author = quote_item.css('.author::text').extract()
        #     tags = quote_item.css('.tag::text').extract()
        #     yield {
        #         'quote': quote,
        #         'author': author,
        #         'Tags': tags
        #         }