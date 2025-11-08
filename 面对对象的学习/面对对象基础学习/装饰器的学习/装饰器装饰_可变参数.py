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


# 需求：定义一个可以计算多个数据和列表values值的函数，并添加友好提示。

# 定义装饰器
def fn_outer(fn_name):
    def fn_inner(*args,**kwargs):
        print('正在努力计算中')
        return fn_name(*args,**kwargs)
    return fn_inner
# 定义原函数
@fn_outer
def get_sum(*args,**kwargs):
    '''
    该函数用于计算数字列表和字典value的值之和
    :param args: 数字列表
    :param kwargs: 字典 键是字符串 值是数字
    :return: 求和结果
    '''
    # sum=0
    # for i in args:
    #     sum=sum+i
    # for v in kwargs.values():
    #     sum=sum+v
    # 注释的代码和没注释的代码效果是一样的
    return sum(args)+sum(kwargs.values())


# 调用函数
sum = get_sum(1,2,3,a=4,b=5,c=6)
print(sum)

'''
sum() 函数的能力
Python内置的 sum() 函数可以处理任何可迭代对象（iterable），包括：
列表（list）
元组（tuple）
集合（set）
等等...
# 这些都是有效的
sum([1, 2, 3])     # 列表 → 6
sum((1, 2, 3))     # 元组 → 6
sum({1, 2, 3})     # 集合 → 6
'''