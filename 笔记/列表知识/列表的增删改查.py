'''
列表的追加
lst=[]
lst.append('赵本山')   # 追加一个元素
print(lst)   ['赵本山']
lst.extend(['武则天','嬴政'])
print(lst)   ['赵本山', '武则天', '嬴政']  # 追加多个元素

列表的插入
lst.insert(0,'赵敏')
print(lst)   ['赵敏', '赵本山', '武则天', '嬴政']

列表的删除
lst.pop(0)
print(lst)   ['赵本山', '武则天', '嬴政']
a = lst.pop(0)
print(a)  # 赵敏
lst.remove('赵本山')
print(lst)   ['赵敏', '武则天', '嬴政']

列表的修改
lst[0] = '开'
print(lst)   ['开', '赵本山', '武则天', '嬴政']

 列表的查询
print(lst[0])   赵敏
num = list.count('赵敏')
print(num)   1  表示列表中赵敏这个元素出现过一次
'''

# 列表练习的小案例  将所有姓张的人改为姓王
list = ['张无忌','张绍刚','武则天']
# print(len(list))   3    0 1 2 三个元素长度为3
for i in range(len(list)):
    # print(i) 0 1 2 len的值为3 i循环的赋值就是0 1 2
    name = list[i]  # 列表的索引通过数字 i的赋值为0 1 2 对应着列表中从左往右数的三个元素的数字
    # print(name)   #name 为list[i]的变量
    if name.startswith('张'):
        # 判断名字的首字母是否为张
        new_name = '王'+name[1:]
        # 如果名字的首字母是张 就将张改为王 name中的 1 2 两个元素对应的名不变
        print(new_name)
        list[i] = new_name
        # 将列表中的名字替换为新名字
print(list)















