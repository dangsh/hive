import requests
import re
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='5801200zxg',
    db='noveltest',
    charset='utf8'
)
cursor = conn.cursor()

def getSortNovelList():
    response = requests.get('http://www.quanshuwang.com/list/1_1.html')
    response.encoding = 'gbk'
    result = response.text
    reg = r'<a target="_blank" title="(.*?)" href="(.*?)"'
    novelUrlList = re.findall(reg , result)
    return novelUrlList

def getNovelInfo(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
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

    return imgUrl , sort , author , status , chapterUrl , description

def getChapterList(url):
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

for novelName , novelUrl in getSortNovelList():
    imgUrl , sort , author , status , chapterListUrl , description = getNovelInfo(novelUrl)
    cursor.execute("insert into novel (sortname , name , imgurl , description , status , author) values ('{}' , '{}' , '{}' , '{}' , '{}' , '{}')" .format (sort , novelName , imgUrl , description , status , author))
    conn.commit()
    lastrowid = cursor.lastrowid #插入数据的ID值
    for chapterUrl , chapterName in getChapterList(chapterListUrl):
        chapterContent = getChapterContent(chapterUrl)
        cursor.execute("insert into chapter(novelid , title , content) values({} , '{}' , '{}')".format(lastrowid , chapterName , chapterContent))
        conn.commit()
conn.close()