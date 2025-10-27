# match...case语句(结构化模式匹配语句)和if语句有很多相似但功能更强大


'-------------匹配字面值--------------------'
# 通过match...case语句实现一个判断今天是星期几的例子
from datetime import datetime   # 导入日期模块
day = datetime.today().weekday()  # 获取星期对应的数据 0是星期一 1是星期二 。。。。。

match day:
    case 0:
        print('今天是星期一，新的一周开始了')
    case 4:
        print('今天是星期五，今天工作完就放假了')
    case 5|6:
        print('今天是周末，不用工作')
    case _:
        print('今天是工作日，该上班了')

'----------------绑定变量---------------------------'
# 当math...case语句出现变量时，这个变量就会尽可能的匹配match的变量，并且还会为match中的变量赋值。
a = 10086
match a:
    case b:  # 设置变量b 接收a中的数据
        print('我是b我被赋值为',b)

# 我是b我被赋值为 10086
# 由打印的结果可match的中的变量b被赋值为变量a中的数据
# b就是match中的变量，a变量将数据赋值给了b，b内包含a的数据


# 除了绑定单个变量，match...case语句还可以匹配列表或者元组中的变量  但并不会区分列表和元组因此他们的结果是相同的
point = eval(input('请输入坐标(格式为x,y):'))  # eval()可以将传入的字符串作为表达式执行 不会因为 input 而将数据变为整数
match point:
    case(0,0):
        print(f'{point}这是原点')
    case(0,y):
        print(f'Y轴的坐标是{y}')
    case(x,0):
        print(f'X轴的坐标是{x}')
    case(x,y):
        print(f'X轴的坐标是{x}，Y轴的坐标是{y}')


'--------------约束项(if语句)------------------------'
# 在实现case匹配项时，可以添加一个if语句来作为该case的约束项。如果if语句判断成功，则执行该case的匹配；相反贼不执行匹配，并继续寻找下一个case匹配项
points = eval(input('请输入坐标(格式为x,y):'))
match points:
    case(x,y) if x>y:
        print(x,y,'x大于y')
    case (x, y) if y>x :
        print(x,y,'y大于x')
    case (x, y) if x == y:
        print(x, y, 'x等于y')


'-----------------匹配字典-------------------------'
# 在match...case 语句中还可以实现字典的匹配，当匹配字典时，只匹配case中提到的结构就可以了，后续的键值对会被忽略
dict = {'a':1,'b':2}
match dict:
    case{'a':1}:
        print('字典中存在想匹配的数据，匹配成功')

# 如果想要获取没有匹配到的键值对需要用到 **通配符进行获取

dict1 = {'c':3,'d':4}
match dict1:
    case{'c':3,**data}:   # **通配符后面的数据就是存储没有匹配到的键值对的数据的变量
        print(data)  # {'d': 4}

# 如果想要匹配原字典中键值对中的值，可以使用变量进行匹配
dict2 = {'e':5,'f':6}
match dict2:
    case{'e':data_1,'f':data_2}:  # 通过匹配键 设置变量接收匹配到的键的值
        print(data_1,data_2)  # 5 6


















