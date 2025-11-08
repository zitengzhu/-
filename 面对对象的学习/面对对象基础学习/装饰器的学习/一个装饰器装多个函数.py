'''
案例：演示带参数的装饰器
记忆：
    1.一个装饰器的参数有且只能有一个
    2.如果装饰器有多个参数，可以在该装饰器的外边再包裹一层，把该装饰器当作起其内部函数返回即可
'''

# 需求定义一个装饰器，既可以进行加法运算又可以进行减法运算，即带有参数的装饰器
def logging(flag):
    def fn_outer(fn_name):
        def fn_inner(a,b):
            if flag == '+':
                print('正在进行[加法]运算....')
            elif flag == '-':
                print('正在进行[减法]运算....')
            return fn_name(a,b)
        return fn_inner
    return fn_outer


# 定义原函数，表示加法运算
@logging('+')
def get_sum(a,b):
    return a+b


# 定义原函数，表示减法运算
@logging('-')
def get_sub(a,b):
    return a-b



# 测试
print(get_sub(10,2))
print(get_sum(1,4))
