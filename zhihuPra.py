#.TopstoryItem--experimentButton
import requests
from bs4 import BeautifulSoup
import pandas
newsary = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
res = requests.get('https://www.zhihu.com/topic' , headers = headers)
print(res)
print("1111111111111111111111111111111111")
soup = BeautifulSoup(res.text , 'html.parser')
print("2222222222222222222222222222222222")
print(soup)
print("4444444444444444444444444444444444")

for news in soup.select('.feed-content'):
    print("333333333333333333333333333333333333")
    print(news)