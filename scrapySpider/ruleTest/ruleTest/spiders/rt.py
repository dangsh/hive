from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from ruleTest.items import RuletestItem
 
class DoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["book.douban.com"]
    start_urls = ['https://book.douban.com/']
 
    rules = (
        Rule(LinkExtractor(allow=('subject/\d+',)),callback='parse_items'),
    )
 	

    def parse_items(self, response):
        items = RuletestItem()
        items['name'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()
        items['author'] = response.xpath('//*[@id="info"]//a/text()').extract()
        data = {'book_name':items['name'],
                'book_author':items['author']
                }
        print(data)