import requests
from bs4 import BeautifulSoup
import pandas

newsary = []


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html) 
# print (soup.prettify())
# print(soup.title)
# print(soup.head)
# print(soup.a)
# for child in soup.descendants:
#     print(child)
# print(soup.head)
# print("------------------------")
# print(soup.head.string)

# print(soup.html)
# print("---------------------")
# print(soup.html.string)
# print("--xxxxxxxxxx-----")
# for string in soup.stripped_strings:
#     print(repr(string))

content = soup.head.title.string
for parent in  content.parents:
    print( parent.name)