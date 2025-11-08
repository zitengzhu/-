'---------------------创建用于计算的属性---------------------------'
'''
在python中，可以通过 @property(装饰器)将一个方法转化为属性，以实现用于计算的属性。将方法转化为属性后，可以直接通过方法名来访问方法
无需在访问时再添加小括号，这样可以让代码更加简洁
'''

class Rect:
    def __init__(self,width,height):  # 创建方法
        self.width = width  # 创建实例属性  矩形的宽
        self.height = height # 创建实例属性 矩形的高
    @property   # 将方法转化为属性
    def area(self):
        return self.height*self.width  # 计算面积
rect = Rect(100,100)
# print('面积为',rect.area)   # 调用area方法 运行数据返回面积的值并进行打印  面积为 10000
# 如果不加 @property 将方法转化为属性 在访问方法时就要加小括号
'''
通过@property转化后的属性不能被重新赋值，如果对其赋值就会报错
例：
rect.area=50  # 对属性进行赋值
print(rect.area)AttributeError: property 'area' of 'Rect' object has no setter
'''


'--------------------为属性添加安全保护机制-----------------------------'
'''
在python中，默认情况下创建的类属性或者实例是可以在类体外进行修改的。如果想要限制它在体外被修改，可以将他设置为私有
如果想要创建一个可以被读取，但不能被修改的属性，可以使用@property实现只读
'''

'''
class TVshow:  # 创建类
    def __init__(self,show):  # 初始化 设置方法
        self.__show = show   # 设置私有
    @property  # 将方法转化为属性
    def show(self):   # 定义show方法
        return self.__show  # 返回show的值
tvshow = TVshow('正在播放《满江红》')  # 创建实例  正在播放《满江红》是show的值  
print(tvshow.show)  # 正在播放《满江红》  show方法接收的是self.__show的返回值 使用tvshow这个实例名访问方法

# 进行修改
tvshow.show = '正在播放《将进酒》'
print(tvshow.show)
# AttributeError: property 'show' of 'TVshow' object has no setter
# 由以上代码可知通过上述方式创建的代码属性是只读不能修改
'''

# 通过属性不仅可以将属性设置为只读属性，还可以为属性设置拦截器，即允许属性进行修改，但修改需要遵守一定的约束
class TVshow:  # 定义类
    list_film = ['满江红','流浪地球2','绝地反击','无名']  # 设置类属性
    def __init__(self,show):
        self.__show = show  # 设置私有
    @property  # 将方法转化为属性
    def show(self):
        return self.__show  # 返回属性值
    @show.setter  # 设置setter方法让属性可以修改
    def show(self,value):
        if value in TVshow.list_film:  # 进行判断
            self.__show = print('你选择了《',value,'》这部电影')  # 值负责打印
            self.__show = value  # 进行数据存储
            # 如果不加  self.__show = value 进行数据储存 那么函数在运行
            # self.__show = print('你选择了《',value,'》这部电影') 之后并不会储存 打印完了就没了
            # tvshow.show中存储的就是None  如果想在修改完属性之后可以访问需要将他存储起来
            # 而 self.__show = value 就是将value中的数据存储到了 self.__show中
            # 数据如果不存储就访问就会返回None
        else:
            print('没这个电影')

tvshow = TVshow('正在播放《满江红》')  # 创建实例
# 这里的 '正在播放《满江红》' 会传递给 __init__ 方法的 show 参数，然后赋值给 self.__show
print(tvshow.show)
# 访问show方法会返回self.__show的值 最终显示正在播放《满江红》
print('你可以从',TVshow.list_film,'中选择影片')  # 调用类属性
tvshow.show='绝地反击'  # 修改属性
print(tvshow.show,'稍后播放')  # 获取修改后的属性














