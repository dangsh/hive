# -*- coding: utf-8 -*-

# Scrapy settings for ali project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ali'

SPIDER_MODULES = ['ali.spiders']
NEWSPIDER_MODULE = 'ali.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ali (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

FEED_EXPORTERS_BASE = {
    'json' : 'ali.tojson.chongxie' ,
    'jsonlines' : 'scrapy.contrib.exporter.JsonLinesItemExporter',

}

# IPPOOL = [{'ipaddr': '211.159.177.212:3128'}, {'ipaddr': '166.111.80.162:3128'}, {'ipaddr': '139.217.24.50:3128'}, {'ipaddr': '119.27.177.169:80'}]
IPPOOL = [{'ipaddr': '211.159.177.212:3128'}]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':300,
    'ali.middlewares.MyproxiesSpiderMiddleware':100

}
RETRY_ENABLED = False

KEY_WORDS = ['女装', '男装', '内衣', '鞋靴', '箱包', '配饰', '运动服饰', '运动装备', '母婴用品', '童装', '玩具', '工艺品', '宠物', '园艺', '日用百货', '办公文教', '汽车用品', '食品饮料', '餐饮生鲜', '家纺家饰', '家装建材', '美容化妆', '个护家清', '3C', '手机', '家电', '电工电气', '照明', '仪表', '包装', '印刷纸业', '电子元器件', '安防', '机械', '五金工具', '劳保', '橡塑', '化工', '精细', '钢材', '纺织皮革', '医药' ,'橡胶' ,'皮草' ,'皮鞋' ,'秋裤' ,'外套' ,'电梯' ,'阁楼' ,'鱼' ,'狗' ,'猫' ,'龟' ,'兔' ,'鼠' ,'牛' ,'羊' ,'鸡' ,'猪' ,'肉' ,'骨' ,'蛋白' ,'矿物质' ,'代餐' ,'健康' ,'绿色' ,'卡通' ,'毛绒' ,'酒' ,'币' ,'卡' ,'灯' ,'照明' ,'草坪' ,'沥青' ,'文艺' ,'刀' ,'护具' ,'飞行' ,'叉' ,'棍' ,'网' ,'鱼竿' ,'凯夫拉' ,'卡扣' ,'安全' ,'插座' ,'电线' ,'袜子' ,'娃娃' ,'靠垫' ,'鞋垫' ,'屏幕' ,'塑料' ,'宝石' ,'植物' ,'玻璃水' ,'死飞' ,'汽车' ,'电动车' ,'自行车' ,'胸牌' ,'打印机' ,'文具' ,'笔' ,'扫帚' ,'拖把' ,'肥皂' ,'洗发水' ,'项链' ,'平安扣' ,'吊坠' ,'桌子' ,'椅子' ,'壁纸' ,'涂料' ,'颜料' ,'饮料' ,'水' ,'家具' ,'餐具' ,'瓷器' ,'瓷砖' ,'鲜花' ,'沙' ,'塑料' ,'五金' ,'钢材' ,'磁铁' ,'贴纸' ,'玻璃' ,'键盘' ,'鼠标' ,'杯子' ,'手机' ,'纸' ,'花卉' ,'绿植' ,'酱油' ,'土豆' ,'辣椒' ,'醋' ,'糖']
# KEY_WORDS = ['内衣']

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ali.middlewares.AliSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ali.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ali.pipelines.AliPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
