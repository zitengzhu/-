'''
案例：
    装饰器装饰_有参无返回的原函数
细节：
    装饰器的内部函数格式要和被装饰的原函数保持一致，
    即：原函数是无参无返回的，则装饰器的内部函数也必须是无参无返回的。
       原函数是无参有返回的，则装饰器的内部函数也必须是无参有返回的。
       原函数是有参无返回的，则装饰器的内部函数也必须是有参无返回的。
       原函数是有参有返回的，则装饰器的内部函数也必须是有参有返回的。
'''


# 需求：定义有参有返回的get_sum()函数，在不改变其代码的基础上，添加友好提示：正在努力计算中

# 定义装饰器
def fn_outer(fn_name):
    def fn_inner(a,b):
        print('正在努力计算中')
        return fn_name(a,b)
    return fn_inner
# 语法糖写法
# 定义原函数
@fn_outer
def get_sum(a,b):
    return a+b

print(get_sum(10,20))

# 传统写法
# get_sum = fn_outer(get_sum)
# sum = get_sum(10,20)
# print(f'求和结果为：{sum}')
