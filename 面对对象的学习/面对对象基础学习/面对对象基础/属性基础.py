# 属性的添加
'''
类外设置对象的属性：
    对象名.属性名=属性值
    特点：该属性独属于这个对象，即：该类的其他对象没有这个属性
类外获取对象的属性：
    对象名.属性名
'''

'''
class Car:  # 定义汽车类
    def run(self):  # 定义run行为
        print('汽车会跑')

# 创建实例对象
car = Car()
# car.run()  汽车会跑
# 类外定义属性   这个定义的属性只能car实例调用 其他的用不了
# car.color = '绿色'
# 类内访问属性
# print(car.color)  绿色


# 创建实例对象
car1 = Car()
# 数据重写
car.run = '汽车坏了'
# print(car.run)  汽车坏了
'''

'''
类内获取属性值：
    self.属性
'''


class Car:  # 定义汽车类
    def run(self):  # 定义run行为
        print('汽车会跑')

    def show(self):
        self.run()
        print(f'我是show属性,我在调用{self.run()}方法')


car = Car()
car.show()
'''
汽车会跑
汽车会跑
我是show属性,我在调用None方法

打印结果的解释：
    调用show方法时self.run()为类内调用方法 执行一次run方法
    在python中如果遇见大括号 python会优先识别大括号内的代码 
    print方法中的花括号内的数据为self.run() python识别到他之后又执行一次 run方法
    这就是会有两个汽车会跑的原因
    
    self.run() 方法没有用 return 语句返回任何值，所以默认返回 None
    执行 self.run() → 打印"汽车会跑"
    self.run() 执行完毕，返回 None
    Python把 None 放到花括号的位置
    最终打印：我是show属性,我在调用None方法
'''
