#输入身高、体重、年龄、性别
height=input("请输入身高（m）：")
weight=input("请输入体重（kg）：")
age=input("请输入年龄：")
sex=input("请输入性别（男为1，女为0）：")
#数据类型转换
height=float(height)
weight=float(weight)
age=int(age)
sex=int(sex)
#计算体脂率
#BMI=体重（kg）/（身高*身高）（米）
#体脂率=1.2*BMI+0.23*年龄-5.4-10.8*性别（男为1，女为0）
bmi=weight/(height*height)
tzl=1.2*bmi+0.23*age-5.4-10.8*sex
#判定正常成年人的的体脂率是男性15%-18%，女性为25%-28%
#不用判断语句
#男女均相差10%=0.1
min=0.15+0.10*(1-sex)
max=0.18+0.10*(1-sex)

result=min<tzl<max
print("你得体脂率是%f" % tzl)
print("你得体脂率是否符合标准",result)