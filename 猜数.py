#准备数据
num=500
count=0
while True:
    #输入一个结果
    count+=1
    result=input("请输入结果")
    result=int(result)
    #进行比对
    if result==num:
        print("恭喜你猜对了，答案就是%d,总共猜了%d次"%(result,count))
        exit()#或者break
    if result>num:
        print("你猜的数字太大了")
    else :
        print("你猜的数字太小了")