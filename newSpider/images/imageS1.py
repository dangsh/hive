import os
import requests
import time
import random
from lxml import etree

# 166.111.80.162	3128
# 211.159.177.212	3128
# 123.116.242.190	8118
# 120.26.14.14	3128

keyWord = input(f"{'Please input the keywords you want to download :'}")
class Spider():
    def __init__(self):
        self.headers = {
            "User-Agent" :  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        }
        self.filePath = ('/Users/张霄港/Desktop/hive/newSpider/images/' + keyWord + '/')

    def creat_File(self):
        filePath = self.filePath
        if not os.path.exists(filePath):
            os.makedirs(filePath)

    # 获取图片的数量
    def get_pageNum(self):
        total = ""
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc").format(keyWord)
        html = requests.get(url)
        selector = etree.HTML(html.text)
        pageInfo = selector.xpath('//header[@class="listing-header"]/h1[1]/text()')
        string = str(pageInfo[0])
        numlist = list(filter(str.isdigit , string))
        for item in numlist:
            total += item
        totalPagenum = int(total)
        return totalPagenum

    def main_function(self):
        #count是总图片数   #times是总页面数
        self.creat_File()
        count = self.get_pageNum()
        print("We have found:{} images!".format(count))
        times = int(count/24 + 1)
        j = 1
        for i in range(times):
            pic_Urls = self.getLinks(i+1)
            for item in pic_Urls:
                self.download(item , j)
                j += 1

    #获取链接
    def getLinks(self , number):
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}").format(keyWord,number)
        try:
            html = requests.get(url)
            selector = etree.HTML(html.text)
            pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
            print(pic_Linklist)
        except Exception as e:
            print(repr(e))
        return pic_Linklist

    #下载图片
    def download(self , url , count):
        # 例 https://alpha.wallhaven.cc/wallpaper/616442/thumbTags
        string = url.strip('/thumbTags').strip('https://alpha.wallhaven.cc/wallpaper/')
        html = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + string + '.jpg'
        pic_path = (self.filePath + keyWord + str(count) + '.jpg')
        try:
            pic = requests.get(html , headers = self.headers)
            f = open(pic_path , 'wb')
            f.write(pic.content)
            f.close()
            print("Image:{} has been downloaded!".format(count))
            time.sleep(random.uniform(0 , 2))
        except Exception as e:
            print(repr(e))

spider = Spider()
spider.main_function()