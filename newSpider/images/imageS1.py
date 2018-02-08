import os
import requests
import time
import random
from lxml import etree

# 166.111.80.162	3128
# 211.159.177.212	3128
# 123.116.242.190	8118
# 120.26.14.14	    3128

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
        string = str(pageInfo[0]) #获取到带有图片数量的语句
        numlist = list(filter(str.isdigit , string)) #逐个取出数字
        for item in numlist:
            total += item
        totalPagenum = int(total) #将数字拼接成数量，转换成int类型
        return totalPagenum #返回图片数量

    def main_function(self):
        #count是总图片数   #times是总页面数
        self.creat_File() #创建文件夹
        count = self.get_pageNum() #获取到图片的数量
        print("We have found:{} images!".format(count))
        times = int(count/24 + 1) #计算出总页面数
        j = 1
        for i in range(times):
            pic_Urls = self.getLinks(i+1) #获取图片url
            for item in pic_Urls:
                self.download(item , j) #调用下载图片方法
                j += 1

    #获取链接
    def getLinks(self , number):
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}").format(keyWord,number)
        try:
            html = requests.get(url)
            selector = etree.HTML(html.text)
            pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
            print(pic_Linklist) #获取到图片url
        except Exception as e:
            print(repr(e))
        return pic_Linklist

    #下载图片
    def download(self , url , count):
        # 例 https://alpha.wallhaven.cc/wallpaper/616442/thumbTags
        string = url.strip('/thumbTags').strip('https://alpha.wallhaven.cc/wallpaper/')
        # 239227
        # http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-616442.jpg
        html = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + string + '.jpg'
        print(html)
        # /Users/张霄港/Desktop/hive/newSpider/images/dog1.jpg
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