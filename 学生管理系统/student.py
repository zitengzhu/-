'''
该文件用于记录学生类，学生的属性信息为：姓名，性别年龄，手机号，描述信息
'''

# 定义学生类
class Student:
    def __init__(self,name,gender,age,phone,describe):
        self.name=name
        self.gender=gender
        self.age=age
        self.phone=phone
        self.describe=describe
    def __str__(self):
        return f'姓名:{self.name},性别:{self.gender},年龄:{self.age},手机号:{self.phone},评语:{self.describe}'

if __name__ == '__main__':
    s=Student('张三','男','18','1111111','炎龙铠甲合体')
    print(s)
