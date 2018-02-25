import requests
import json

'''
/ : 将返回数据库中的所有代理
/?country=China :针对国家的条件进行结果过滤
/?type=http :针对代理类型进行结果过滤
/?anonymity=normal_anonymity :将返回匿名程度大于等于查询条件的代理，
    其中transparent<normal_anonymity<high_anonymity
/?num=100 :将按代理的匿名和往返时间排序，返回前100个代理
'''

url = 'http://proxy.nghuyong.top/?num=50'
response = requests.get(url)
data = json.loads(response.text)
print(type(data))

for i in range(len(data['data'])):
    print(data['data'][i]['ip_and_port'])
# print(response.text)
