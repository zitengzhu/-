'''
self关键字介绍

self简介：
    概述：
        它是python的内置关键字，用于表示当前对象的引用
    作用：
        1个类可以有多个对象,这多个对象都可以通过 对象名. 的方式访问类中的行为(函数)
        函数默认有self属性,函数通过self来区分到底是哪个对象对用的该函数
    大白话：
        谁调用函数,self就代表哪个对象
    总结：
        在类外访问类中的方法 需要通过对象名.的方式询问
        在类内访问类中的方法 需要通过self.的方法询问

'''

'''
# 类外调用函数
class Car:
    def run(self):
        print('self的值是',self)
car = Car()
# 调用类中的方法
car.run()
# self的值是 <__main__.Car object at 0x000001F842590110>
print(f'car的地址值{car}')
# car的地址值<__main__.Car object at 0x000001F842590110>

car是Car类的实例 car实例调用类的run方法 run方法中的self就代表car 
'''

# 类内调用self
class Car:
    def run(self):
        print(f'{self}的汽车会跑')
    def work(self):
        print(f'我是work函数，我的self值是{self}')
        self.run()  # self代表本类当前对象的引用
car = Car()
car.work()
car.run()
# 我是work函数，我的self值是<__main__.Car object at 0x000002278C424450>
# <__main__.Car object at 0x000002278C424450>的汽车会跑  # 类内调用run方法
# <__main__.Car object at 0x0000015BE7F34450>的汽车会跑  # 类外调用run方法
'''
由上述代码可知 类内 内外调用方法 car实例的地址值不变
类内调用的数据传输路径：
    car实例调用work方法，work方法的self就是car实例，self.run()中self就是car实例 
    self.run()其实就是car.run
类外调用的数据传输路径：
    car实例通过对象名.的方法调用run方法 run方法的self就是car实例
'''