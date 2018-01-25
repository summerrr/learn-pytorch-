import requests
import re  #正则表达式
import urllib #下载
for n in range(3):
   url='http://www.htqyy.com/genre/musicList/3?pageIndex=1&pageSize=20&order=hot'
   html =requests.get(url)
   data=re.findall('value="(.*?)"><span',html.text)
   for m in data:
       url2='http://f1.htqyy.com/play6/'+str(m)+'/mp3/1'
       urllib.requires.urlretrieve(url2,'d:\\'+m+'mp3')#下载音乐




