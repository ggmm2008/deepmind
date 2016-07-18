# -*- coding:utf-8 -*-  

import feedparser
import re
from ipdb import set_trace
import jieba

def getwordcounts(url):
    
    d=feedparser.parse(url)
    wc={}
    for e in d.entries:
        if 'summary' in e:
            summary=e.summary
        else:
            summary=e.description
    #set_trace()
    words=getwords(e.title+' '+summary)
    for word in words:
        wc.setdefault(word,0)
        wc[word]+=1
    return d.feed.title,wc


def getwords(html):
    word=[]
    wordG=jieba.cut(html,cut_all=False)
    for k in wordG:
        #set_trace()
        for i in range(len(k)):
            is_chinese_value=True
            if is_chinese(k[i])==False:
                is_chinese_value=False
                break
        if is_chinese_value==True:
            print k
            word.append(k)
    #print word
    #set_trace()
    return word

def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        #set_trace()
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False


#set_trace()
apcount={}
wordcounts={}
feedlist=[line for line in file('feedlist.txt')]
for feedurl in feedlist:
    title,wc=getwordcounts(feedurl)
    print title
    wordcounts[title]=wc
    for word,count in wc.items():
        apcount.setdefault(word,0)
        if count>1:
            apcount[word]+=1

wordlist=[]
for w,bc in apcount.items():
    frac=float(bc)/len(feedlist)
    if frac>0.1 and frac<0.5 :wordlist.append(w)

set_trace()
out=file('blogdata.txt','w')
out.write('BLOG')
for word in wordlist:
    print word
    out.write(word.encode('utf-8'))
    out.write('\t')
out.write('\n')
for blog,wc in wordcounts.items():
    out.write(blog)
    for word in wordlist:
        if word in wc:out.write('\t%d' % wc[word])
        else:out.write('\t0')
    out.write('\n')