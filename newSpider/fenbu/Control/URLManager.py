from Spider.UrlSpider import getUrl , r
from Spider.spider1 import getCntent as g1
from Spider.spider2 import getCntent as g2
from multiprocessing import Process
import threading
import  time

getUrl()
while r.llen("url"):
    t1 = threading.Thread(target=g1 , args=(r.rpop("url") ,))
    t2 = threading.Thread(target=g2 , args=(r.rpop("url") ,))
    time.sleep(2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

print(r.lrange("url" , 0 , -1))