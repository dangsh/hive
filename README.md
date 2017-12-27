## hive (虫巢)
## 概述

这是一个 我个人用于练习python爬虫的项目：
1.用于自己练习
2.可供大家参考


#### 说明：我会在空闲的时候学习爬虫并且上传

## 1.qidainTop500
用于爬取起点月票榜前500名的，书名，作者，类型，简介，更新，书籍url
<!-- ![Alt text](pic1.png) -->
已经初步完成

## 2.doubanTop250
用于爬取豆瓣电影榜前250名的，影片名字，导演，评分，评价人数 等信息
已经初步完成

## 3.zhihupra  
准备爬知乎的信息。。。正在做。。。。。还未完成

## 4.doubanBook
用于爬取豆瓣图书榜前250名的，书籍名字，作者，评分，评价人数 等信息
已经初步完成

## 5.lagou
用于爬取拉勾网的招聘信息，薪资，工作地点，要求等
目前仅完成了单独python类工作的爬取，正在进行改良，以抓取全部的类型。
还需要学习怎么应对反爬虫的方法

## 6.lagouPlusP
在lagou的基础上升级了，用于爬取所有工作的信息，不只是python工作的信息
是一只大型的爬虫，但是还需要再进行优化来提高速度，因为上万条数据需要的时间太久
之后会学习分布式爬虫，使用代理池，等方法进行优化
lagouPlusP.xlsx文件储存了简单测试的结果，gongzuo.xlsx储存了所有的（315条）工作类型网址和名称
#经过改良之后：
理论上应该可以爬取到整个网站15000条左右的招聘信息
进行了简单的测试，爬取到了3000多条数据储存在 lagouPlusp.xlsx文件之中
在之后还会对这个爬虫进行一些改良

## 整合了文件夹的结构
创建了两个文件夹 1.beautiSoupSpider  2.scrapySpider
将之前的文件放入了 beautiSoupSpider

## 7.scrapySpider/First
利用scrapy框架重写了拉钩爬虫，极大程度上提高了性能
十秒左右可以爬取到4000条数据，并且做了简单的反反爬虫处理
还会进行一些升级

## 8.scrapySpider/First
升级了First的功能，添加了反反爬虫，20分钟左右爬取到了8万条数据
速度感人，并且没有被屏蔽
添加了一个honey文件夹，存储爬取到的数据，以后数据分析可以使用

## 9.scrapySpider/xxx
用于练习middlewares 和 webdriver PhantomJS 爬取动态数据，并且写博客进行记录
每天都会运行一下First爬虫，继续获取数据 2017 11 25

## 10.scrapySpider/mongoTest
测试将爬取的数据存储在MongoDB中，学习MongoDB的用法

## 11.scrapySpider/company
获取黄页上软件行业中的信息，企业名称，类型，法人信息等
实现了大部分功能 2017 11 28
将数据放入MongoDB中，练习MongoDB的使用 
再次更新后添加了换页的操作，可以获得所有页数上的数据，爬虫基本完成了
将数据存入了MongoDB中，但是为了方便查看又运行了一次，放入json文件，3700余条数据
2017 12 1

## 12.scrapySpider/KrSpider
爬取36kr的实时资讯

## 13.newSpider/bilibili
请求接口，获取bilibili直播的弹幕内容，简单实现

## 14.newSpider/novel
全站爬虫，爬取全书网所有小说信息及内容并入库
spider2 更新了spider，可以获取全站的数据，并且保存到数据库
2017 12 25

## 15.scrapySpider/companyP
改进爬虫，爬取整个网站的信息