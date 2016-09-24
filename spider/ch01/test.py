from urllib import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://roll.mil.news.sina.com.cn/col/zgjq/index.shtml")
bsObj=BeautifulSoup(html.read())
finds=bsObj.findAll('a',{'href':re.compile('\/china\/')})
for find in finds:
    print (find['href'])
#print(bsObj.h3)
