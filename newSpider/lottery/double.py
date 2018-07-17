import requests
from lxml import etree
import re
import matplotlib.pyplot as plt
from pandas import Series

url = "http://datachart.500.com/ssq/history/newinc/history.php?start=00001&end=18081"
response = requests.get(url)
response = response.text
selector = etree.HTML(response)
reds = []
blues = []
for i in selector.xpath('//tr[@class="t_tr1"]'):
    datetime = i.xpath('td/text()')[0]
    red = i.xpath('td/text()')[1:7]
    blue = i.xpath('td/text()')[7]
    for i in red:
        reds.append(i)
    blues.append(blue)

s_blues = Series(blues)
s_blues = s_blues.value_counts()
s_reds = Series(reds)
s_reds = s_reds.value_counts()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x(), 1.02*height, "%s" % height)

fig = plt.figure()
labels = s_blues.index.tolist()
sizes = s_blues.values.tolist()
rect = plt.bar(range(len(sizes)) , sizes , tick_label = labels)
autolabel(rect)
plt.show()

labels2 = s_reds.index.tolist()
sizes2 = s_reds.values.tolist()
rect2 = plt.bar(range(len(sizes2)), sizes2 , tick_label = labels2)
autolabel(rect2)
plt.show()

