SPIDER_MODULES = ['fenbu.spiders']
NEWSPIDER_MODULE = 'fenbu.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

#使用scrapy-redis里面的去重组件.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis里面的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停后,能保存进度
SCHEDULER_PERSIST = True

# 指定排序爬取地址时使用的队列，
# 默认的 按优先级排序(Scrapy默认)，由sorted set实现的一种非FIFO、LIFO方式。
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline':400,
    'fenbu.myPipeLines.mongoPipe.MongopipClass':300,
}

# 指定redis主机
REDIS_HOST='192.168.8.88'
REDIS_PORT=6379

# 指定mongo
MONGO_HOST = "192.168.14.90"
MONGO_PORT = 27017
MONGO_DBNAME = "ali"
MONGO_COLLECTION = "fenbu_test"
