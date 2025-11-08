# 需求：发表评论前，需要先登录，再验证验证码

# 定义装饰器，实现登录
def check_login(fn_name):
    def fn_inner():
        print('正在登录...')
        fn_name()
    return fn_inner
# 定义装饰器，实现验证验证码
def check_code(fn_name):
    def fn_inner():
        print('正在检验验证码...')
        fn_name()
    return fn_inner
# 原函数
# 语法糖写法
@check_login
@check_code
def comment():
    print('发表评论')

comment()
# 正在登录...
# 正在检验验证码...
# 发表评论


# 传统写法
# c1 = check_code(comment)
# c1这行代码打印结果为
# 正在检验验证码...
# 发表评论
# c2 = check_login(c1)
# c2这行代码加入的正在登录...会打印在正在检验验证码...的上面
# c2()
