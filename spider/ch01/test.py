#coding:utf-8
from urllib import urlopen
from bs4 import BeautifulSoup
import re
import socket

def getLinks(articleUrl):
    html=urlopen(articleUrl)
    bsObj=BeautifulSoup(html.read())
    return bsObj.findAll('a',{'href':re.compile('\/\/')})

def main():
    articleUrl="http://roll.mil.news.sina.com.cn/col/zgjq/index.shtml"
    links=getLinks(articleUrl)
    s=r'\/\/(?P<hostname>[0-9a-zA-Z.]+)(/)?'
    for link in links:
        if 'href' in link.attrs:
            #print link
            m=re.search(s,link.attrs['href'])

            print (link.attrs['href'])
            #print m.group(0)
            #print m.group('hostname') 
            url2ip(m.group('hostname') )

def url2ip(url):
    print url
    ip=''
    try:
        ip=socket.gethostbyname(url)
        print ip
    except:
        print 'url error'
    return ip

main()