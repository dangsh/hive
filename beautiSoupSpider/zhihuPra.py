#.TopstoryItem--experimentButton

# author:trendhu
# time:2017-11-9
import requests
from bs4 import BeautifulSoup
newsary = []
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    "Cookie":'q_c1=24ed61471954429696f439ccb03c95ab|1509695338000|1509695338000; _zap=cdfc7372-09e7-45d9-9b73-bfbc9bdc795a; d_c0="ABCC6mNTpQyPTgXQJSgwSS-hvaKw7R7f2xY=|1510033253"; aliyungf_tc=AQAAAJl/s01dSwwAy8ugewu6UroXring; r_cap_id="YjZkYmVmOTAzYjZhNDRkYTkyZjI1MzMyMjM3MDM1Yzc=|1510223889|8b5dedbdd81c7d8056f175a3b0601c82c4bda838"; cap_id="MzQ1NDNlYjM0OTA3NGY1NzgzZTAwYjI2OTUwM2ExZGU=|1510223889|5e9886af4ee8c72167b0de32c1f0330a91dda4d4"; _xsrf=34779d003a75d8391bb48bc1846b0e38; z_c0=Mi4xa251LUF3QUFBQUFBRUlMcVkxT2xEQmNBQUFCaEFsVk5rSDd4V2dCc1JmMjFtdHZLTEJHbFlJZ1A2THU0U0hMUXBR|1510224016|de108c55fc634d2e8b48e5093d0a7a50f456b999; __utma=51854390.1499785568.1510033253.1510033253.1510223895.2; __utmb=51854390.0.10.1510223895; __utmc=51854390; __utmz=51854390.1510033253.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100--|2=registration_date=20161127=1^3=entry_date=20161127=1'
}
res = requests.get('https://www.zhihu.com/topic' , headers = headers)
print(res.text)
# print("1111111111111111111111111111111111")
# soup = BeautifulSoup(res.text , 'html.parser')
# print("2222222222222222222222222222222222")
# print(soup)
# print("4444444444444444444444444444444444")

# for news in soup.select('.feed-content'):
#     print("333333333333333333333333333333333333")
#     print(news)