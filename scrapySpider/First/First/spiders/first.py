import scrapy
from First.items import FirstItem


class SpiderMan(scrapy.Spider):
    name = "rose"
    start_urls = [
        "https://wenku.baidu.com/"
    ]

    def parse(self , response):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        # for item in response.xpath("//div/dl/dt/a"):
        #     title = item.xpath("text()").extract()
        #     targetUrl = item.xpath("@href").extract()

        #     oneItem = FirstItem()
        #     oneItem["title"] = title
        #     oneItem["targetUrl"] = targetUrl
        #     print(oneItem)
            


        for item in response.xpath("//div/dl/dd/a"):
            title = item.xpath("text()").extract()
            targetUrl = item.xpath("@href").extract_first()

            oneItem = FirstItem()
            oneItem["title"] = title
            oneItem["targetUrl"] = targetUrl
            # url = "https://wenku.baidu.com/" + oneItem["targetUrl"]
            # yield oneItem
            yield scrapy.Request(url = "https://wenku.baidu.com/list/71"  , meta = {"title":title} , callback=self.parse_url)

    def parse_url(self , response):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        title = response.meta["title"]
        print(title)

        for sel2 in response.xpath('//a[@class="Author logSend"]'):
            docName = sel2.xpath("text()").extract()

            oneItem = FirstItem()
            oneItem["docName"] = docName

            print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
            print(oneItem["docName"])
