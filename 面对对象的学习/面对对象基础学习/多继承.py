# 多继承是就近原则 子类括号内有多个父类先访问离子类近的如果没有在从左到右依次调用
# 当一个类有多个父类时，默认使用第一个父类的属性和方法，
# 可以使用 类名.__mro__ 或者 类名.mro() 查看调用的先后顺序

class a:
    pass


class b:
    pass


class C(a, b):  # 先在C类中找 如果没有在从左到右找
    pass


print(C.mro())  # [<class '__main__.C'>, <class '__main__.a'>, <class '__main__.b'>, <class 'object'>]
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.a'>, <class '__main__.b'>, <class 'object'>)


'''
子类调用父类方法：
    子类中仍想要保留父类的行为，则需要在子类中调用父类方法.可以直接使用父类名来调用，使用的方法： 
    父类名.父类方法名(self)
        精准访问，想找哪个找哪个
    super().父类函数名() 
        只能访问最近的那个父类，没有往后继续查找
'''
# 父类名.父类方法名(self)

# 父类1
class Master:
    def __init__(self):
        self.kongfu = '古法煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 父类2
class School:
    def __init__(self):
        self.kongfu = '标准化煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 子类
class Student(Master,School):
    def __init__(self):
        self.kongfu='独创煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_Master_cake(self):
        Master.__init__(self)  # self依旧是0x01
        Master.make_cake(self)

# 创建实例对象
xiaoming = Student()
# 调用自己的make_cake方法
xiaoming.make_cake()  # 运用独创煎饼果子制作煎饼果子
# 调用Master父类的make_cake方法
xiaoming.make_Master_cake()  # 运用古法煎饼果子制作煎饼果子
# 调用自己的make_cake方法
xiaoming.make_cake()  # 运用古法煎饼果子制作煎饼果子

'''
注释：
    调用Student子类创建xiaoming这个实例  假设地址值为0x01
    第一次调用 make_cake 方法调用的是自己的make_cake方法 self就是0x01 print(f'运用{self.kongfu}制作煎饼果子')中的self.kongfu就是Student子类自己的self.kongfu值 独创煎饼果子 打印的结果就是:运用独创煎饼果子制作煎饼果子
    
    第二次调用 make_Master_cake 方法 执行过程为： 先执行 Master.__init__(self)这个代码 因为 调用的是xiaoming这个实例的方法所以 self依旧是0x01  那么在父类Master中 self就变为了0x01  
    所以 子类Student中的elf.kongfu='独创煎饼果子' 被重写为 self.kongfu = '古法煎饼果子' 属性发生了改变  Master.make_cake(self) 内的 print(f'运用{self.kongfu}制作煎饼果子') 中的self.kongfu 就是 古法煎饼果子
    打印的结果就是:运用古法煎饼果子制作煎饼果子
    
    第三次调用 make_cake 方法调用的是自己的make_cake方法 self就是0x01  但因为属性发生了重写self.kongfu就不是独创煎饼果子了而是古法煎饼果子 输出结果为：运用古法煎饼果子制作煎饼果子
'''

# super().父类函数名() 可以自动查找父类，适合单继承使用多继承不建议

class Master1:
    def __init__(self):
        self.kongfu = '古法煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 父类2
class School1:
    def __init__(self):
        self.kongfu = '标准化煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 子类
class Student1(Master,School):
    def __init__(self):
        self.kongfu='独创煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_other_make(self):
        super.__init__()  # 只能访问最近的那个父类，没有往后继续查找 子类继承的多个父类中最近的是Master super就是Master
        # super.__init__() 就是Master.__init__()
        super().make_cake()
        # super().make_cake() 就是 Master.make_cake()



