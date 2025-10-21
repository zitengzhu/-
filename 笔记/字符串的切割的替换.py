'''
                                        .strip()的学习
s='  你好   ，  我是你白   '
s1=s.strip()
print(s)  #  你好   ，  我是你白    不加   .strip()的话在你好的前面和你白的后面的空格也会被打印
print(s1)  # 你好   ，  我是你白    加上   .strip()的话在你好的前面和你白的后面的空格不会被打印

user_name=input('请输入用户名')
pass_word=input('请输入密码')
if  user_name=='admin':
    if pass_word==('123456'):
        print('登录成功')
    else:
        print('用户名或密码输入错误')
else:
    print('用户名或密码输入错误')
    
在 user_name 和 pass_word 中如果输入过程中如果前后出现空格也会显示登录失败  

user_name=input('请输入用户名').strip()
pass_word=input('请输入密码').strip()
if  user_name=='admin':
    if pass_word==('123456'):
        print('登录成功')
    else:
        print('用户名或密码输入错误')
else:
    print('用户名或密码输入错误')

#  在input('请输入用户名')和input('请输入密码')后加上.strip之后 输入过程中在最前面和最后面加入了空格键不会报错
# .strip会删除输入文字前面和后面的  空格,\t,\n

'''

                                         # 字符串的替换
# replace() 字符串替换的关键字
# s='你好，我是张三'
# s1=s.replace('张三','李四')
# print(s)   # 你好，我是张三
# print(s1)  # 你好，我是李四

# a = '你好，  我是王五  。'
# a1 = a.replace(' ','')  # 取消掉字符串文字之间的空格
# print(a)  # 你好，  我是王五  。
# print(a1)  # 你好，我是王五。


                                      # 字符串的切割
# .split() 是字符串切割的关键字
s = 'python_java_c_c#'
s1 = s.split('_')
print(s1)
# ['python', 'java', 'c', 'c#']将s中的'python_java_c_c#' 通过.split()切割后会根据切割的内容形成一个列表 每个内容都是列表中单独的值




