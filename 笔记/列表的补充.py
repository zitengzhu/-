'''
# 列表会按照你存放的顺序进行保存
lst=[110, 50,60,88,44,66]
print(lst)  #[110, 50, 60, 88, 44, 66]
#列表的paix
lst.sort()
print(lst)  #[44, 50, 60, 66, 88, 110]
#列表的降序
lst.sort(reverse=True)
print(lst)  #[110, 88, 66, 60, 50, 44]

#列表的嵌套
lst=['sda','sdad',['sdad','sdawdad',['dadad','frfrwada']],'sdada']
#       0      1      2.0      2.1      2.2.0   2.2.1          3

lst[1].upper()
print(lst[1])  # sdad  列表中的元素每一个都是字符串 字符串不可变 

lst[1]=lst[1].upper()
print(lst[1])  # SDAD
#将let[1] 转化为大写后 设置一个新变量并打印新变量
print(lst[2][1])  # sdawdad
print(lst[2][2][1])  # frfrwada


# 列表的循环删除
list = ['狼牙','赵民','张无忌','张绍刚','武则天']
for i in list:
    if i.startswith('张'):
        list.remove(i)
print(list)  # ['狼牙', '赵民', '武则天']

for i in range(len(list)):
    print(list[i])
# 狼牙
# 赵民
# 张绍刚
# 武则天

#列表是通过数字进行索引的 用for循环直接打印列表列表不会改变  需要通过列表的索引进行才能达到第二个for循环的效果
'''





#                          列表的循环删除
list = ['狼牙','赵民','张无忌','张绍刚','武则天']
temp = []  # 建立一个新的列表
for i in list:
    if i.startswith('张'):
        # list.remove(i)  有bug
        temp.append(i)  # 将要删除的内容存放在新列表中
        print(temp)  # ['张无忌', '张绍刚']
for i in temp:  # 设置变量 i 来循环新的列表 i 就是  ['张无忌', '张绍刚']
    list.remove(i)  # 在列表中删除 i 变量代表的值
print(list)   # 打印删除i代表的值后的结果 ['狼牙', '赵民', '武则天']

















