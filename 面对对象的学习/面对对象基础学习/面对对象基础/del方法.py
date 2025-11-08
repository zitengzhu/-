'''
案例：
    演示del方法的使用

__del__()：
    当.py文件执行结束，或者手动调用del方法时，会自动调用该函数
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
    def __del__(self):
        print('对象被删除')

car = Car('红色',4)
del car # 手动调用del函数 del方法被调用
# 不加del的话 在.py文件执行完毕之后也会自动调用del

'''
执行上述代码发现在程序结束时 __str__ 被调用输出结果为
颜色:红色,轮胎数量:4对象被删除的原因是：
    当Python看到 f'{self}对象被删除' 时：
    它需要把 self（car对象）变成文字 (变为car实例 因为car实例被打印str方法自动执行)
    要变成文字，就会自动调用这个对象的 __str__ 方法
    __str__ 返回："颜色:红色,轮胎数量:4"
    所以最终打印："颜色:红色,轮胎数量:4对象被删除"
总结：
    只要把对象放在 f-string 的 {} 里，或者用 print(对象)，就会自动调用 __str__ 方法。
    所以不是 del car 直接调用了 __str__，而是在 __del__ 方法里的 f'{self}' 调用了它。
解决方法：
    直接打印对象被删除避免打印对象
'''