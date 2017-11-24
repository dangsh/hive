import scrapy
from First.items import FirstItem

class Lagou(scrapy.Spider):
    name = "forth"
    start_urls = [
        "https://www.lagou.com/zhaopin/Java/"
    ]
    

    def parse(self , response):
        for item in response.css('div:not(#content-container) h1'):
            jobMessage = item.css('::text').extract()
            print(jobMessage)
