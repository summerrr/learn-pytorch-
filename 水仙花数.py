while True:
    #输入数据
    num=input("请输入一个三位数值")
    #数据有效性验证
    #if len(num)==3:针对字符串可以这样验证
    num = int(num)
    if not (100<num<999):
        print("你输入的数据无效,直接退出程序")
        exit()
    #分解数值
    bai=num//100
    shi=num%100//10
    ge=num%10
    #判定是否为水仙花数
    result=(bai**3+shi**3+ge**3==num)
    #打印结果
    if result:
        print("%d是水仙花数"%num)
    else:
        print("%d不是水仙数" %num)