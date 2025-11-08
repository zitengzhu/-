'''
在python中，可以为属性和方法设置私有权限，即设置某个属性和方法不继承子类。
设置私有属性和方法的方式：在属性或方法名前面加上__，格式：
    # 私有属性:
        __属性名
    # 私有方法:
        def __方法名()

私有属性和方法使用规则：
    只能在类的内部使用，不能在类的外部使用
    如果想在类的外部使用通过公共接口

私有属性不能直接访问，在python中一般定义方法名'get_xx'来获取私有属性，定义方法名'set_xx'来用来修改私有属性

'''

'''
案例：演示封装之私有属性
    
封装简介：
    概述：
        属于面对对象的三大特征之一，就是隐藏对象的属性和实现细节，仅对外提供公共的访问方式
    怎么封装：
        函数，类都是封装的体现
    好处：
    1.提高代码的安全性。   由私有化来保证
    2.提高代码的复用性。   由函数来保证        
    弊端：
        代码量增加了，因为私有内容外界想访问，必须提高公共的访问方式，代码量就增加了
'''

class Master:
    def __init__(self):
        # 手艺
        self.cook_cake = '创新煎饼果子配方'
        # 私房钱
        self.__money = '10000'  # 设置为私有
    def make_cake(self):
        print(f'用{self.cook_cake}制作煎饼')
    def get_money(self):
        return self.__money
    def set_money(self,money):
        self.__money = money


class Student(Master):
    pass


if __name__ == '__main__':
    xm = Student()
    xm.set_money(100)
    # 100为Master类中set_money方法中的形式参数给形式参数赋值self.__money接受形式参数数据self.__money的值就变为了100
    print(xm.get_money())
