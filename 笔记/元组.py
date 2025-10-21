#元组是不可变的列表   固定了某些数据，不允许外界修改就可以用元组
tuple_1=(1,2,3,4)
print(tuple_1)  # (1, 2, 3, 4)
print(tuple_1[0])  # 1
print(tuple_1[1:3])  # (2, 3)
print(type(tuple_1))  # <class 'tuple'>
'''
tuple_1[0]=6 会报错
原因：
元组类型的对象不支持元素的重新定义 元素不可变
'''


#元组如果只有一个元素
tuple_2=('哈哈')
print(type(tuple_2))  # <class 'str'>  {括号默认是优先级  print((1+1)*3)=6}
tuple_3=('哈哈',)
print(type(tuple_3))  # <class 'tuple'> 元组内只有一个元素可以加个，让 数据类型从str变为tuple


tuple_4=('a','b',['c','d'])
tuple_4[2].append('7')
print(tuple_4)  # ('a', 'b', ['c', 'd', '7'])
#元组内的列表位置不可变但可以在列表内增加内容