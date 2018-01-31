# import requests
# import re
# import redis
#
# def getUrl():
#     r = redis.Redis(host='localhost' , port='6379' , decode_responses=True)
#
#     for page in range(10):
#         url = "https://movie.douban.com/top250?start=" + str(page * 25) + "&filter="
#         response = requests.get(url)
#         response = response.text
#         reg = '<a href="(.*?)" class="">'
#         result = re.finditer(reg , response)
#         for i in result:
#             # i.groups()[0]
#             r.set('url',i.groups()[0])
#     print("--------像redis中添加数据完成--------")
#     print(r.get('url'))  # 取出键name对应的值
#     print(type(r.get('url')))
import redis
r = redis.Redis(host='localhost' , port='6379' , db=5 ,decode_responses=True)
# r.lpush('xx' ,'zhangsan')
# r.lpush('xx' ,'lisi')
# r.lpush('xx' ,'wangwu')
print(r.rpop('xx'))
