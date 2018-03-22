from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
 
class DoubanSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["book.douban.com"]
    start_urls = ['https://book.douban.com/top250']
 
    rules = (
        Rule(LinkExtractor(allow=('subject/\d+/$',)),callback='parse_items',follow=True),
    )

    def parse_items(self, response):
        pass

