
dict = {'aaa':'bbb','ccc':'ddd','fff':'eee'}
# 直接遍历字典打印只会显示字典的键 不会显示值
# for i in dict:
    # print(i,end=' ')  # aaa ccc fff
# 但可以通过在dict后调用键获取值的数据
# for i in dict['aaa']:
    # print(i,end='')  #bbb


# 使用items()可以获取字典键值对的列表
'''
for i in dict.items():
    print(i)
    ('aaa', 'bbb')
    ('ccc', 'ddd')
    ('fff', 'eee')
'''
'''
# 想要直接获取键值对的数据也可以在遍历字典时加入 key 和value
for key,value in dict.items():
    print(key,value)
    aaa bbb
    ccc ddd
    fff eee  
'''