import re
'==========================================================================='
# 初步学习re模块

res = re.findall('a','我是abc,我今年18岁,我有2000块')
# print(res)   # ['a']  筛选出来的是列表



res_1 = re.findall(r'\d+','我是abc,我今年18岁,我有2000块')
# print(res_1)  # ['18', '2000'] '\d+'前加入r 是为了防止转意



res_2 = re.finditer(r'\d+','我是abc,我今年18岁,我有2000块')
# print(res_2)   <callable_iterator object at 0x00000185556FEAD0>  iterator是迭代器
for i in res_2:  # 设置循环可以从迭代器中拿到内容
    '''
    print(i)
    <re.Match object; span=(9, 11), match='18'>
    <re.Match object; span=(15, 19), match='2000'>
    
    在i后面加上.group可以直接从匹配的结果中拿到想要的数据 
    print(i.group())
    print(type(i.group()))  
    18
    2000
    <class 'str'>
    '''

res_3 = re.search(r'\d+','我叫周杰伦,今年32岁,我的年级是5年4班')
# print(res_3)  <re.Match object; span=(8, 10), match='32'>  search 只会匹配到第一次匹配到的内容
# print(res_3.group())  # 32  加上.group可以直接从匹配的结果中拿到想要的数据


res_4 = re.match(r'\d+','我叫周杰伦,今年32岁,我的年级是5年4班')
# print(res_4)  # None   match在匹配的时候是从字符串的开头开始进行匹配的，类似于在正则前加^

# 预加载  提前把正则对象加载完毕
obj = re.compile(r'\d+')  # 设置的正则
# 正则设置之后把加载好的正则直接进行使用
res_5 = obj.findall('我叫周杰伦,今年32岁,我的年级是5年4班')
# print(res_5)  # ['32', '5', '4']

'=================================================================='
# re模块 提取分组数据

# 目标字符串
s = (
    "<div class='西游记'><span id='10010'>中国联通</span></div>"
    "<div class='西游记'><span id='10086'>中国移动</span></div>"
     )
# 预加载 想要设置的正则变量  "<span id='\d+'>.*?</span>"  id='\d+' 意为匹配在id=后面的重复一次及以上的数字  .*?为惰性匹配 匹配的是 >< 之间最少的字符数据
# obj = re.compile("r<span id='\d+'>.*?</span>")
# res_6 = obj.findall(s)
# print(res_5)   ["<span id='10010'>中国联通</span>", "<span id='10086'>中国移动</span>"]

# 加入小括号的元字符 可以筛选信息单独提取内容 使目标数据更简洁
# obj = re.compile("r<span id='(\d+)'>(.*?)</span>")
# res_6 = obj.findall(s)
# print(res_5)     [('10010', '中国联通'), ('10086', '中国移动')]

# ?P<> 可以给匹配的目标数据起名字 P是大写的 名字就是<>中的设置的变量   (?P<id>\d+) 就是把所有匹配到的数字数据放入id这个变量的组里  (?P<name>.*?) 同理
obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")
res_6 = obj.finditer(s)
# finditer 获取的是迭代器 设置循环可以获取迭代器内的数据
for i in res_6:
    # 设置变量接受预加载内设置的组里的数据
    id = i.group('id')
    print(id)
    # 设置变量接受预加载内设置的组里的数据
    name = i.group('name')
    print(name)



























