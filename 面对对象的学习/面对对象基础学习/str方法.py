'''
案例：
    str方法的用法

__str__()方法：
    当用print()函数打印对象的时候，会自动调用该对象(所在类)的str方法
'''
class Car:
    def __init__(self,color,number):
        self.color = color
        self.number = number
    def show(self):
        print(f'颜色:{self.color},轮胎数量:{self.number}')
    # str方法默认打印地址值，无意义，一般会重写，改为打印对象的属性值
    def __str__(self):
        # 返回属性值
        return f'颜色:{self.color},轮胎数量:{self.number}'

car = Car('红色',4)  # 定义属性值
# car.show()  颜色:红色,轮胎数量:4  用的较少
print(car)  # 颜色:红色,轮胎数量:4  返回car的属性值   用的较多
# 当用print()函数打印对象的时候，会自动调用该对象(所在类)的str方法
# 打印car 自动调用了car所在的Car类的str方法
print('\n')
car1 = Car('绿色',5)  # 定义属性值
# car1.show()  颜色:绿色,轮胎数量:5  用的较少
print(car1)  # # 颜色:绿色,轮胎数量:5   返回car1的属性值  用的较多
# 当用print()函数打印对象的时候，会自动调用该对象(所在类)的str方法
# 打印car1 自动调用了car1所在的Car类的str方法




