#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib2
import re
Page=1
story=[]
count=0
filename='storyfile1.txt'

count1=0
nu=1

Headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)',
         'Referer':'http://www.qiushibaike.com/hot/'}
while count<120:
    url='https://www.douban.com/doulist/2520779/?start='+str(count)+'&sort=time&sub_type='
    try:
        request=urllib2.Request(url,headers=Headers)
        response=urllib2.urlopen(request)
        contence=response.read()#.decode('UTF-8')
        pattern=re.compile('<div class="source">.*?</div>.*?<div class="post">.*?<a href="https://movie.douban.com/subject/.*?" target="_blank">.*?<img width="100" src=".*?/>.*?</a>.*?</div>.*?<div class="title">.*?<a href="https://movie.douban.com/subject/.*?" target="_blank">(.*?)</a>.*?</div>.*?<div class="abstract">(.*?)</div>.*?</div>',re.S)
        items=re.findall(pattern,contence)
        for item in items:
            story=story+([item[0],item[1]])

    except urllib2.URLError,e:
        if hasattr(e,'code'):
            print e.code
        if hasattr(e,'reason'):
            print e.reason
    count=count+25
f=open(filename,'w')
for i in story:
    i=i.strip()
    i=i.replace('<br />','')
    line='\n\r'+i+'\n\r'
    count1=count1+1
    if not count1%2:

        line=line+'\n\r\n\r\n\r******************************************************\r\n'+'美剧'+str(nu)+'\r\n\r\n'
        nu=nu+1
    f.write(line)
f.close()
          
