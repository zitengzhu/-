import random
import time
'''
1.游戏的开始和结束设置
2.游戏开始后的随机字符输出
3.用户输入字符和系统输出字符进行对比
4.用户输入后的正确与错误的反馈
5.计算游戏总时间
6.结算
'''
while True:
    user=input('请输入x开始游戏(按a结束游戏)')
    if user =='x':
        print('游戏开始')
        stare_time=time.time()
        str = ('qwertyuiopasdfghjklzxcvbnm')
        new_list = random.sample(str, 3)
        # random随机输出的是列表  input输入的是字符串
        # print(new_list)  # list
        new_str = ''.join(new_list)
        # 通过.join将列表转化为字符串并与用户输入的字符进行比较
        # print(type(new_str))  # <class 'str'>
        print(new_str)
        use=input('请输入对应的字符')
        if use == new_str:
            end_time=time.time()
            cha_time=end_time-stare_time
            print('恭喜你回答正确共花费',cha_time)
        else:
            print('对不起回答错误请重新输入')
    elif user =='a':
        print('游戏结束')
        break
    else:
        print('对不起请重新输入')



