#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib2
import re
Page=1
story=[]
count=0
filename='storyfile1.txt'
url='http://www.qiushibaike.com/hot/page/'+str(Page)

Headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)',
         'Referer':'http://www.qiushibaike.com/hot/'}
while Page<36:
    try:
        url='http://www.qiushibaike.com/hot/page/'+str(Page)
        request=urllib2.Request(url,headers=Headers)
        response=urllib2.urlopen(request)
        contence=response.read()#.decode('UTF-8')
        pattern=re.compile('<span class="touch-user-name-a">(.*?)</span>.*?<div class="content-text">.*?href=.*?<span>(.*?)</span>.*?div id="qiushi_counts.*?class="laugh-comment" data-votes="(.*?)".*?<span class="comments">.*?<a href="javascript:.*?id=.*?class.*?article>',re.S)
        items=re.findall(pattern,contence)
        for item in items:
            story=story+([item[0],item[2],item[1]])

    except urllib2.URLError,e:
        if hasattr(e,'code'):
            print e.code
        if hasattr(e,'reason'):
            print e.reason
    Page=Page+1
f=open(filename,'w')        
for i in story:
    
    line='\n\r'+i+'\n\r'
    if len(line)>30:
        count = count +1
        line=line+'\n\r\n\r\n\r******************************************************\r\n'+'story'+str(count)+'\r\n\r\n'
    f.write(line)
f.close()
