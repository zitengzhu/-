'''
案例：
    减肥案例
需求：
    例：小明同学当前100kg，每当他跑一跑步体重就会下降0.5kg，每当他大吃大喝一次体重就会增加2kg
    利用面对对象计算小明体重
分析：
    类名：Student
    对象名：小明
    属性：体重
    方法：跑步 大吃大喝
'''

class Student:
    def __init__(self):  # 进行初始化
        self.current_weight = 100  # 定义体重100 每当设置一个实例默认体重都是100
    def run(self):
        print('跑步一次体重下降0.5kg')
        self.current_weight-=0.5
    def eat(self):
        print('大吃大喝一次体重增加2kg')
        self.current_weight+=2
    def __str__(self):
        return f'当前体重为{self.current_weight}kg'

# 创建实例
xiaoming = Student()
# 跑步
xiaoming.run()
xiaoming.run()
# 大吃大喝
xiaoming.eat()
# 当前体重
print(xiaoming)