import requests   #网络请求
import time  #时间
import random   #随机数


class GetMSG:
    def __init__(self):
        self.url='https://zhuanlan.zhihu.com/api/columns/sspaime/followers'
        self.header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        self.f=open('D:\\python projects\\test\\data\\data.txt','a')

    def getFenSi(self,data):
        self.html=requests.get(self.url,params=data,headers=self.header)
        #提取数据批量提取
        for n in range(len(self.html.json())):
        #print(self.html.status_code)
             self.hash=self.html.json()[n]['hash']
             self.f.write(self.hash+'\n'*2)

    def fclose(self):
        self.f.close()
if __name__=='__main__':
   getmsg=GetMSG()
   for m in range(0,100,20):
       data={'limit':20,'offset':m}
       getmsg.getFenSi(data)
    #或者GetMSG.getFenSi(getmsg)
   getmsg.fclose()