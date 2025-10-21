s = '你好，我是周杰伦'

res = s.find('周')
print(res)  # 打印的结果是正数说明结果在这里面

res_1 = s.find('菜')
print(res_1)  # 打印的结果为负数说明结果不在这里面

res_2 = s.index('周')
print(res_2)  # 打印的结果是正数说明结果在这里面

#res_3 = s.index('菜')  # 程序报错说明结果不在字符串里面
#print(res_3)

print('周' in s)  # 返回为Ture则在字符串里 反之不在
print('周' not in s)  # 返回为False则在字符串里 反之不在

msg=input('请输入你的信息')
if msg.startswith('祝'):
    print('验证通过')
else:
    print('验证失败')
# .startswith可以判断文字的开头
# .endswith可以判断文字结尾(不常用)

money=input('请输入你的存款')
if money.isdigit():
    money=int(money)
    print('你的钱是整数')
else:
    print('你的钱不是整数')
# .isdigit 可以判断你输入的是不是整数
# .isdecimal 可以判断你输入的是不是小数



