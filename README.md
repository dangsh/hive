hive (虫巢)
===========================

## 概述
这是一个 我个人用于练习python爬虫的项目：<br/>
1.用于自己练习<br/>
2.可供大家参考<br/>

## 环境依赖<br/>
python 3.6.2<br/>

## 以下为可选:<br/>
scrapy<br/>
requests<br/>
bs4 <br/>
pandas<br/>
MongoDB <br/>
MySQL 5.7 <br/>

## 部署步骤<br/>
1. 安装python3.6.2<br/>
2. 通过pip安装 scrapy , requests , bs4 , pymysql 等模块<br/>


## 目录结构描述 <br/>
├── beautiSoupSpider               // bs4爬虫 <br/>
├── scrapySpider                   // scrapy爬虫 <br/>
├── newSpider                      // 使用requests完成的其它功能 <br/>
└── README.md                      // 帮助文档 <br/>

## V0.0.1 版本内容 beautiSoupSpider <br/>
1. qidainTop500  <br/>
    用于爬取起点月票榜前500名的，书名，作者，类型，简介，更新，书籍url<br/>
2. doubanTop250<br/>
    用于爬取豆瓣电影榜前250名的，影片名字，导演，评分，评价人数 等信息已经初步完成<br/>
3. doubanBook<br/>
    用于爬取豆瓣图书榜前250名的，书籍名字，作者，评分，评价人数 等信息已经初步完成<br/>
4. lagou<br/>
    目前仅完成了单独python类工作的爬取，正在进行改良，以抓取全部的类型。还需要学习怎么应对反爬虫的方法<br/>
5. lagouPlusP<br/>
    在lagou的基础上升级了，用于爬取所有工作的信息，不只是python工作的信息是一只大型的爬虫，<br/>
    但是还需要再进行优化来提高速度，因为上万条数据需要的时间太久之后会学习分布式爬虫，使用代理池，等方法进行优化<br/>
    lagouPlusP.xlsx文件储存了简单测试的结果，gongzuo.xlsx储存了所有的（315条）工作类型网址和名称<br/>
5.1 经过改良之后：<br/>
    理论上应该可以爬取到整个网站15000条左右的招聘信息<br/>
    进行了简单的测试，爬取到了3000多条数据储存在 lagouPlusp.xlsx文件之中<br/>
    在之后还会对这个爬虫进行一些改良<br/>

## V0.0.2 版本内容 scrapySpider <br/>
1. First<br/>
    利用scrapy框架重写了拉钩爬虫，极大程度上提高了性能十秒左右可以爬取到4000条数据<br/>
    并且做了简单的反反爬虫处理还会进行一些升级<br/>
2. First<br/>
    升级了First的功能，添加了反反爬虫，20分钟左右爬取到了8万条数据.速度感人，并且没有被屏蔽<br/>
    添加了一个honey文件夹，存储爬取到的数据，以后数据分析可以使用<br/>
3. xxx<br/>
    用于练习middlewares 和 webdriver PhantomJS 爬取动态数据<br/>
4. mongoTest<br/>
    测试将爬取的数据存储在MongoDB中，学习MongoDB的用法<br/>
5. company<br/>
    获取黄页上软件行业中的信息，企业名称，类型，法人信息等。实现了大部分功能 2017 11 28<br/>
    将数据放入MongoDB中，练习MongoDB的使用 <br/>
    再次更新后添加了换页的操作，可以获得所有页数上的数据，爬虫基本完成了<br/>
    将数据存入了MongoDB中，但是为了方便查看又运行了一次，放入json文件，3700余条数据<br/>
    2017 12 1<br/>
6. KrSpider<br/>
    使用chromeDriver模拟浏览器操作，爬取36kr的实时资讯<br/>
7. companyP<br/>
    改进爬虫，爬取整个网站的信息<br/>
8. weibo<br/>
	目标是爬取所有微博用户的信息！！<br/>
	现在已经成功拿到了一些数据，但是由于请求过于频繁，被封了ip。<br/>
	使用了http代理，user-Agent ,cookie 但是还是不行。<br/>
	明天继续！ 2018-2-10<br/>
	事实上发现自己犯了一个很sb的错误，解决了BUG，明天爬取下一层的信息2018-2-10<br/>


## V0.0.3 版本内容 newSpider <br/>
1. bilibili<br/>
    请求接口，获取bilibili直播的弹幕内容，简单实现<br/>
2. novel<br/>
    全站爬虫，爬取全书网所有小说信息及内容并入库<br/>
    spider2 更新了spider，可以获取全站的数据，并且保存到数据库<br/>
    2017 12 25<br/>
3. jd<br/>
    使用splinter,模拟登录jd，秒杀商品<br/>
4. weibo<br/>
    使用splinter,模拟登录weibo，自动转发微博<br/>
4. csdn<br/>
	使用selenuim,模拟浏览csdn博客，使用ip代理。IP代理从数据库中获得。<br/>
	更新了一个geturl的简单爬虫，爬取自己博客的url，不需要手动输入了，每次随机取出<br/>
	2018-2-10<br/>
5. fenbu<br/>
	利用redis完成分布式爬虫，爬取豆瓣电影top250<br/>
6. images<br/>
	使用requests下载壁纸网站的图片资源，实现搜索并下载图片<br/>
	2018 2 3<br/>
	使用多线程优化了imageS2爬虫，极大程度上提高了爬取速度<br/>
	2018 2 8<br/>
