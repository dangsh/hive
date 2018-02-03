import requests
import re
import redis
r = redis.Redis(host='localhost', port='6379', db=5, decode_responses=True)
def getUrl():
    for page in range(10):
        url = "https://movie.douban.com/top250?start=" + str(page * 25) + "&filter="
        response = requests.get(url)
        response = response.text
        reg = '<a href="(.*?)" class="">'
        result = re.finditer(reg , response)
        for i in result:
            pass
            r.lpush("url" , i.groups()[0])
    print("--------向redis中添加数据完成--------")

#情况redis中的内容
if __name__ == "__main__":
    print(r.lrange("url" , 0 , -1))
    for i in range(500):
        r.rpop("url")
    print(r.lrange("url" , 0 , -1))


