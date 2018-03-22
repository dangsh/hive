from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from ruleTest.items import RuletestItem
 
class DoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["book.douban.com"]
    start_urls = ['https://book.douban.com/top250']
 
    rules = (
        Rule(LinkExtractor(allow=('subject/\d+/$',)),callback='parse_items',follow=True),
    	Rule(LinkExtractor(allow=('top250?start=\d+/$')),callback='parse_items2',follow=True)
    )
 	

    def parse_items(self, response):
        items = RuletestItem()
        items['name'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()
        items['author'] = response.xpath('//*[@id="info"]//a/text()').extract()
        data = {'book_name':items['name'],
                'book_author':items['author']
                }

    def parse_items2(self , response):
    	response = response.text
    	print(response)

