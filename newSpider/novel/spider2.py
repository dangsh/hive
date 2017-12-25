import requests
import re


def getClassList():
    response = requests.get('http://www.quanshuwang.com/')
    response.encoding = 'gbk'
    result = response.text
    reg = '<li><a href="(.*?)">(.*?)</a></li>'
    classList = re.findall(reg , result)
    classList = classList[:11]
    return classList

def getPage(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = '<em id="pagestats">1/(.*?)</em>'
    page = re.findall(reg , result)
    return page

def getNovelList(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = '<a target="_blank" title="(.*?)" href="(.*?)" class="clearfix stitle">'
    novelList = re.findall(reg , result)
    return novelList

def getNovelPage(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    imgUrl = ""
    sort = ""
    author = ""
    status = "" 
    chapterUrl = ""
    description = ""
    try:
        reg = r'<meta property="og:description" content="(.*?)"/>'
        description = re.findall(reg,result,re.S)[0]
        reg = r'<meta property="og:image" content="(.*?)"/>'
        imgUrl = re.findall(reg,result)[0]
        reg = r'<meta property="og:novel:category" content="(.*?)"/>'
        sort = re.findall(reg,result)[0]
        reg = r'<meta property="og:novel:author" content="(.*?)"/>'
        author = re.findall(reg,result)[0]
        reg = r'<meta property="og:novel:status" content="(.*?)"/>'
        status = re.findall(reg,result)[0]
        reg = r'<a href="(.*?)" class="reader"'
        chapterUrl = re.findall(reg,result)[0]
    except:
        pass
    return imgUrl , sort , author , status , chapterUrl , description

def getNovelChapter(url): #获取章节列表
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    chapterListUrl = re.findall(reg , result)
    return chapterListUrl #每个章节的列表和名称

def getChapterContent(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6'
    chapterContent = re.findall(reg , result , re.S)[0] #re.S python中可以匹配多行
    return chapterContent

for classUrl , className in getClassList():
    page = getPage(classUrl)
    for novelName , novelUrl in getNovelList(classUrl):
        imgUrl , sort , author , status , chapterUrl , description = getNovelPage(novelUrl)
        for chapterUrl , chapterName in getNovelChapter(chapterUrl):
            content = getChapterContent(chapterUrl)
    print(className , classUrl , page)



