# 元组是不可变的列表   固定了某些数据，不允许外界修改就可以用元组
tuple_1=(1,2,3,4)
print(tuple_1)  # (1, 2, 3, 4)
print(tuple_1[0])  # 1
print(tuple_1[1:3])  # (2, 3)
print(type(tuple_1))  # <class 'tuple'>
'''
tuple_1[0]=6 会报错
原因：
元组类型的对象不支持元素的重新定义 元素不可变
但元素可以重新赋值
'''


# 元组如果只有一个元素
tuple_2=('哈哈')
print(type(tuple_2))  # <class 'str'>  {括号默认是优先级  print((1+1)*3)=6}
tuple_3=('哈哈',)
print(type(tuple_3))  # <class 'tuple'> 元组内只有一个元素可以加个，让 数据类型从str变为tuple


tuple_4=('a','b',['c','d'])
tuple_4[2].append('7')
print(tuple_4)  # ('a', 'b', ['c', 'd', '7'])
# 元组内的列表位置不可变但可以在列表内增加内容


'----------------元组的推导式--------------------------'
# 元组的推导式和列表的推导式差不多就是把列表换为了小括号  但元组推导式会 生成生成器
tuples = (i for i in range(0,4))
# print(tuples)   <generator object <genexpr> at 0x000001B1F02845F0>
# 想要获取生成器内的数据可以使用tuple函数生成元组数据  或者使用list函数生成字符串数据
# data = tuple(tuples)
# print(data)  (0, 1, 2, 3)
# data = list(tuples)
# print(data)   [0, 1, 2, 3]


# 想要获取生成器内的数据 还可以使用for循环遍历生成器对象 或者直接使用_next_()方法输出每一个元素，最后将该生成器对象数据
'----------------for循环遍历---------------------'
number = (i for i in range(3))
for i in number:
    print(i,end=' ')
print(tuple(number))
# 0 1 2 ()

'---------------_next_()方法-----------------------------'
number_1 = (i for i in range(3))
print(number_1.__next__())   # 0
print(number_1.__next__())   # 1
print(number_1.__next__())   # 2
print(type(number_1))        # ()

'''
通过for循环遍历和_next_()方法 获取到生成器的数据之后发现原来的生成器对象内的数据已经不存在了 
因此在遍历生成器对象之后如果还想要使用该生成器对象就必须要新建一个生成器对象
'''



