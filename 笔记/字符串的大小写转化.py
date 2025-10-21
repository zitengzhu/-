s = 'python'
s1 = s.capitalize()  # .capitalize() 可以将首字母变为大写
print(s1)  # Python

b = 'I have a dream'
b1 = b.title()  # .title() 可以将每个单词的首字母变为大写
print(b1)   # I Have A Dream

a = 'I HAVE A DREAM'
a1 = a.lower()  # .lower() 可以将大写字母变为小写
print(a1)  # i have a dream

c = 'i have a dream'
c1 = c.upper()  # .upper()可以将小写全部变为大写
print(c1)  # I HAVE A DREAM

# 忽略验证码的大小写进行判断
verify_cod='aBcd1'
# user_input=input('请输入验证码({verify_cod}):')   请输入验证码({verify_cod}):  不加f
user_input=input(f'请输入验证码({verify_cod}):')  # 请输入验证码(aBcd1):  加上f

#为了忽略验证码的大小写可以将 verify_cod 和 user_input 同意转化为大写或者小写
if verify_cod.upper()==user_input.upper():
    print('恭喜你回答正确')
else:
    print('对不起回答错误')
