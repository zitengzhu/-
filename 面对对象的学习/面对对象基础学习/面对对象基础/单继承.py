'''
在编写类时，并不是每次都要从空白开始当要编写的类和另一个已经存在的类之间存在一定地继承关系时，
可以通过继承来达到代码重用的目的，提高开发效率
'''

'------------------------继承的基本语法---------------------------'
#   继承是面对对象编程最重要的特性之一，它源于人们认识客观世界的过程，是自然界普遍存在的一种现象。
#   在程序设计中实现继承，表示这个类拥有它继承的类的所有公有成员或者受保护成员。
#   在面对对象编程中，被继承的类，我们称之为父类或者基类，在他的基础上新建的类，我们称之为子类或者派生类
#   通过继承不仅可以实现代码的重用，还可以通过继承来理顺类与类之间的关系。
#   类名右侧的使用小括号将要继承的基类名称括起来，以实现类的继承
'''
class Fruit:   # 设置的基类
    color = '绿色'   # 定义类属性
    def harvest(self,color):   # 定义方法  设置形式参数
        print('水果是'+color+'的')   # 调用形式参数
        print('水果已经熟了')
        print('原来是是'+Fruit.color+'的')   # 访问类属性的数据

class Apple(Fruit):  # 定义子类  拥有父类的数据
    color = '红色'  # 定义子类的类属性
    def __init__(self):   # 进行初始化  每设置一个实例运行一次里面的代码
        print('\n我是苹果')

class Orange(Fruit):  # 定义子类  拥有父类的数据
    color = '橙色'  # 定义子类的类属性
    def __init__(self):  # 进行初始化  每设置一个实例运行一次里面的代码
        print('\n我是橘子')

apple = Apple()   # 创建实例 并运行初始化时的代码
apple.harvest(apple.color)   # 调用harvest方法()内的apple.color表示访问Apple子类中的color类属性
orange = Orange()   # 创建实例 并运行初始化时的代码
orange.harvest(Fruit.color)  # 调用harvest方法()内的orange.color表示访问Orange子类中的color类属性
'''


'--------------------------方法重写---------------------------'
# 基类成员都会被派生类继承，当基类中的某个方法不完全适用于派生类时需要在派生类中重写父类的方法，
'''
class Fruit:   # 设置的基类
    color = '绿色'   # 定义类属性
    def harvest(self,color):   # 定义方法  设置形式参数
        print('水果是'+color+'的')   # 调用形式参数
        print('水果已经熟了')
        print('原来是是'+Fruit.color+'的')   # 访问类属性的数据

class Apple(Fruit):  # 定义子类  拥有父类的数据
    color = '红色'  # 定义子类的类属性
    def __init__(self):   # 进行初始化  每设置一个实例运行一次里面的代码
        print('\n我是苹果')
    def harvest(self,color):   # 基类Fruit中的方法不适用于这个子类 在子类中重新定义方法
        print('苹果是'+color+'的')   # 调用形式参数
        print('苹果已经熟了')
        print('原来是'+Fruit.color+'的')   # 访问类属性的数据

apple = Apple()  # 创建实例apple  实例可以访问类中的数据  不调用方法的话只会输出 init 中定义的数据
apple.harvest(apple.color)  # 调用harvest方法 访问Apple中的harvest数据


我是苹果
苹果是红色的
苹果已经熟了
原来是绿色的
'''


'---------------派生类中调用基类的init方法--------------------'
# 在派生类中定义 __init__()方法时，不会自动调用基类的__init__方法。
# 如果想要在派生类中调用基类的__init__方法进行必要的初始化，需要在派生类中使用super()函数
'''
class Fruit :
    def __init__(self,color='绿色'):
        Fruit.color = color
    def harvest(self):
        print('水果原来是是',Fruit.color,'的')
class Apple(Fruit):
    def __init__(self):
        print('我是苹果')

apple = Apple()
apple.harvest()


AttributeError: type object 'Fruit' has no attribute 'color'
在基类中调用父类Fruit中的init方法中设置的类属性color会报错 不想报错需要加上 super()函数
'''

class Fruit :  # 设置父类
    def __init__(self,color='绿色'):  # 在init方法中设置颜色参数
        Fruit.color = color   # 将init方法内设置的参数传递到类属性中去
    def harvest(self,color):  # 设置harvest方法
        print('水果原来是是'+Fruit.color+'的')  # 调用基类属性
        print('水果已经熟了')
        print('水果是' + self.color + '的')    # 访问方法内的color参数

class Apple(Fruit):  # 设置子类
    color = '红色'  # 设置子类的类属性
    def __init__(self):  # 设置自己的init方法每创建一个实例运行一次
        super().__init__()  # 调用基类中的init方法
        print('\n我是苹果')


class Sapodilla(Fruit):  # 设置子类
    def __init__(self,color):  # 设置自己的init方法每创建一个实例运行一次
        print('\n我是人参果')
        super().__init__(color)  # 将自身的color数据传递给父类
    def harvest(self,color):  # 重写harvest方法
        print('人参果是',Fruit.color,'的')  # 调用基类中的color数据
        print('人参果成熟了')
        print('现在人参果是',color,'的')  # 调用方法内的color参数

apple = Apple() # 创建一个苹果类的实例
apple.harvest(apple.color)
# 调用harvest函数将Apple子类中的color数据的值传递给基类中的harvest方法内的color参数

sapodilla = Sapodilla('白色') # 创建一个人参果类的实例
# 白色是人参果类中init方法中的color数据的参数  白色 init方法 传递给自己的color数据
# 又经过 super().__init__(color)  将自身的color数据传递给了父类的color数据
# 使得父类中的类属性 color 从绿色变为了白色
sapodilla.harvest('金黄色带紫色条纹')
# 将 '金黄色带紫色条纹'这个数据传递给人参果类中harvest方法中的color数据
