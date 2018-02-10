import os
import requests
import time
from lxml import etree
from threading import Thread

keyWord = input(f"{'Please input the keywords that you want to download:'}")
class Spider():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        }
        self.proxies = {
            "http":"http://166.111.80.162:3128",
        }
        self.filePath = ('/Users/张霄港/Desktop/hive/newSpider/images/' + keyWord + '/')

    def creat_File(self):
        filePath = self.filePath
        if not os.path.exists(filePath):
            os.makedirs(filePath)

    def get_pageNum(self):
        total = ""
        url = ("https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc").format(
            keyWord)
        html = requests.get(url, headers=self.headers, proxies=self.proxies)
        selector = etree.HTML(html.text)
        pageInfo = selector.xpath('//header[@class="listing-header"]/h1[1]/text()')
        string = str(pageInfo[0])
        numlist = list(filter(str.isdigit, string))
        for item in numlist:
            total += item
        totalPagenum = int(total)
        return totalPagenum

    def main_function(self):
        self.creat_File() #创建文件夹
        count = self.get_pageNum() #获取图片总数
        print('We have found: {} images!'.format(count))
        times = int(count/24 + 1) #获取页数
        j = 1 # 计算图片数量
        start = time.time()
        for i in range(times):
            pic_Urls = self.getLinks(i+1) #获取图片的url
            start2 = time.time()
            threads = [] #存放线程
            for item in pic_Urls: #下载图片
                t = Thread(target=self.download , args=[item , j]) #开启线程
                t.start()
                threads.append(t) #将线程放进数组中
                j += 1 #计数
            for t in threads:
                t.join() #启动线程
            end2 = time.time()
            print('This page cost: ',end2-start2 ,'s')
        end = time.time()
        print('Total cost:',end-start ,'s')

    def getLinks(self , number):
        url = (
            "https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}").format(
            keyWord, number)
        try:
            html = requests.get(url, headers=self.headers, proxies=self.proxies)
            selector = etree.HTML(html.text)
            pic_Linklist = selector.xpath('//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
        except Exception as e:
            print(repr(e))
        return pic_Linklist

    def download(self, url, count):
        # 此函数用于图片下载。其中参数url是形如：https://alpha.wallhaven.cc/wallpaper/616442/thumbTags的网址
        # 616442是图片编号，我们需要用strip()得到此编号，然后构造html，html是图片的最终直接下载网址。
        string = url.strip('/thumbTags').strip('https://alpha.wallhaven.cc/wallpaper/')
        html = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + string + '.jpg'
        pic_path = (self.filePath + keyWord + str(count) + '.jpg')
        try:
            start = time.time()
            pic = requests.get(html, headers=self.headers)
            f = open(pic_path, 'wb')
            f.write(pic.content)
            f.close()
            end = time.time()
            print(f"Image:{count} has been downloaded,cost:", end - start, 's')

        except Exception as e:
            print(repr(e))

spider = Spider()
spider.main_function()