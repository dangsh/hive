# -*- coding: utf-8 -*-
import scrapy


class HccSpider(scrapy.Spider):
    name = 'hcc'

    def start_requests(self):
        url = ''
        with open('level3.json', encoding='utf-8') as f:
            for i in range(25254):
                url = f.readline().strip('\n')
                try:
                    yield scrapy.Request(url=url, meta={"url": url}, callback=self.parse2)
                except:
                    pass

    def parse2(self, response):
        url = response.meta["url"]
        response = response.text
        reg = '<span><font>1</font>/(.*?)</span>'
        page = re.findall(reg, response)
        for i in range(int(page[0])):
            new_url = url + "pn" + str(i + 1) + "/"
            # print(new_url)
            try:
                yield scrapy.Request(url=new_url, callback=self.parse3)
            except:
                pass

