'------------添加元素---------------------'
# set_1 = set('aaa')   # 集合内的只能是一个元素
# set_1.add('bbb')
# print(set_1)  {'a', 'bbb'}

'--------------删除元素----------------------------'
# 集合内可以使用del删除整个集合，也可以使用集合的pop()方法或者remove()方法删除一个元素，
# 还可以使用集合对象的clear()方法清除集合，即删除集合内全部元素


set1 = set(['aaa', 'bbb', 'ccc'])
# print(set1)  {'bbb', 'ccc', 'aaa'}
set1.remove('aaa')
# print(set1)  {'bbb', 'ccc'}
set1.pop()  # 默认删除最后一个并返回删除值 括号内是像删除的数据的索引 没有的话默认最后一个
# print(set1)  {'ccc'}
set1.clear()
# print(set1)  set()
