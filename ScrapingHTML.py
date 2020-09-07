Day 7import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
html=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_683818.html').read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('span')
Sum=0
for tag in tags:
    Sum+=int(tag.contents[0])
print(Sum)
