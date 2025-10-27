# 字典的推导式和列表的推导式类似

# 定义数字字典
import random
# :左边的是字典的键 右边的是字典的值          i的值是1-4
dict = {i:random.randint(10,100) for i in range(1,5)}
# print(dict)  {1: 49, 2: 65, 3: 68, 4: 27}


# 直接定义字典
# 定义键
list_1 = ['张三','李四']
# 定义值
list_2 = ['小孩','大人']
# 使用字典推导式生成字典
dict1 = {i:j for i,j in zip(list_1,list_2)}
# print(dict1)  {'张三': '小孩', '李四': '大人'}

