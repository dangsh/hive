from scrapy_redis.spiders import RedisSpider
import re
class MySpider(RedisSpider):
    name = 'mr'

    def parse(self, response):
        response = response.text
        reg = '.html\?offerId=([0-9]*)'
        data = re.findall(reg , response)
        print(data)