# -*- coding: utf-8 -*-

# Scrapy settings for weibo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo'

SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "weibo"
MYSQL_USER = "root"
MYSQL_PASSWORD= "5801200zxg"

IPPOOL = [
    {"ipaddr": "166.111.80.162:3128"},
    {"ipaddr": "202.85.213.220:3128"},
    {"ipaddr": "61.155.164.112:3128"},
    {"ipaddr": "125.62.26.75:3128"},
    {"ipaddr": "39.134.161.13:8080"},
    {"ipaddr": "124.165.252.72:9999"},
    {"ipaddr": "171.34.197.71:3128"},
    {"ipaddr": "34.207.150.171:3128"},
    {"ipaddr": "120.77.223.86:3128"},
    {"ipaddr": "212.49.115.67:8080"},
    {"ipaddr": "14.215.177.73:80"}
]

# IPPOOL = [{'ipaddr': '211.159.177.212:3128'}, {'ipaddr': '139.217.24.50:3128'}, {'ipaddr': '124.165.252.72:80'}, {'ipaddr': '124.165.252.72:8080'}, {'ipaddr': '124.165.252.72:8081'}, {'ipaddr': '124.165.252.72:9999'}, {'ipaddr': '116.211.123.138:80'}, {'ipaddr': '163.177.151.23:80'}, {'ipaddr': '202.100.83.139:80'}, {'ipaddr': '221.7.255.167:80'}, {'ipaddr': '221.7.255.168:80'}, {'ipaddr': '221.7.255.167:8080'}, {'ipaddr': '221.7.255.168:8080'}, {'ipaddr': '112.80.255.32:80'}, {'ipaddr': '220.181.163.231:80'}, {'ipaddr': '163.177.151.162:80'}, {'ipaddr': '14.215.177.58:80'}, {'ipaddr': '123.125.142.40:80'}, {'ipaddr': '180.97.104.14:80'}, {'ipaddr': '223.112.84.30:3128'}, {'ipaddr': '14.215.177.73:80'}, {'ipaddr': '202.85.213.219:3128'}, {'ipaddr': '121.8.98.197:80'}, {'ipaddr': '114.115.140.25:3128'}, {'ipaddr': '121.8.98.198:80'}, {'ipaddr': '61.4.184.180:3128'}, {'ipaddr': '112.80.255.21:80'}, {'ipaddr': '39.137.54.58:8080'}, {'ipaddr': '180.149.131.67:80'}, {'ipaddr': '202.109.237.36:80'}, {'ipaddr': '113.12.72.24:3128'}, {'ipaddr': '183.179.199.225:8080'}, {'ipaddr': '123.125.115.86:80'}, {'ipaddr': '115.239.210.42:80'}, {'ipaddr': '119.28.152.208:80'}]

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
#    'weibo.middlewares.WeiboSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'weibo.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'weibo.pipelines.WeiboPipeline': 300,
}

FEED_EXPORTERS_BASE = {
    'json' : 'weibo.tojson.chongxie' ,
    'jsonlines' : 'scrapy.contrib.exporter.JsonLinesItemExporter',

}

MY_USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    ]

DOWNLOADER_MIDDLEWARES = {
    #    'First.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'weibo.middlewares.MyUserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
     'weibo.middlewares.MyproxiesSpiderMiddleware':125

}

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
