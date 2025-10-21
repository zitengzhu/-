from pyquery import PyQuery

# html = """
# <li class='aaa'><a href='http:/www.baidu.com'>百度</a></li>
# <li class='aaa'><a href='http:/www.googl.com'>谷歌</a></li>
# <li class='ddd' id='qq'><a href='http:/www.jd.com'>京东</a></li>
# <li class='ddd'><a href='http:/www.wy.com'>网易</a></li>
# """

# 加载html的内容
# p = PyQuery(html)
# print(p)  <li><a href="http:/www.baidu.com">百度</a></li>
# print(type(p))  <class 'pyquery.pyquery.PyQuery'>


# pyquery的语法 pyquery的对象直接（css选择器）

# p就是解析完毕的html数据
# a = p('a')
# print(a)  # <a href="http:/www.baidu.com">百度</a>


# 链式操作
# a = p('li')('a')
# print(a)   <a href="http:/www.baidu.com">百度</a>


# 后代选择器
# a = p('li a')
# print(a)     <a href="http:/www.baidu.com">百度</a>

'-----------------------------------------------------------'
# a = p('.aaa')  # .号 是类选择器 等价于 class='aaa'
# print(a)
'''
<li class="aaa"><a href="http:/www.baidu.com">百度</a></li>
<li class="aaa"><a href="http:/www.googl.com">谷歌</a></li>
'''

# a = p('.aaa a')  # aaa后面的空格在css语法中名为后代选择器
# print(a)    # <a href="http:/www.baidu.com">百度</a><a href="http:/www.googl.com">谷歌</a>


# a = p('#qq a')  # #号是id选择器  意为找到id是qq的
# print(a)   <a href="http:/www.jd.com">京东</a>


html = """
    <ul>
        <li class='aaa'><a href='http:/www.baidu.com'>百度</a></li>
        <li class='aaa'><a href='http:/www.googl.com'>谷歌</a></li>
        <li class='ddd' id='qq'><a href='http:/www.jd.com'>京东</a></li>
        <li class='ddd'><a href='http:/www.wy.com'>网易</a></li>
    </ul>
"""
p = PyQuery(html)
href = p('#qq a').attr('href')
text = p('#qq a').text()
# print(href)   http:/www.jd.com
# print(text)     京东

# 坑多个标签同时拿属性默认拿第一个
# 多个标签拿属性
it = p('li a').items()
# print(it)   <generator object PyQuery.items at 0x000001F1F03518A0>  拿到的是迭代器
# 设置循环 拿取数据
for i in it:
    # print(i)   i是所有的a标签
    href = i.attr('href')
    text = i.text()
    print(href,text)


'''
总结:
1 pyquery(选择器（就是要解析的数据）)
2 items()  当选择器选择的内容很多时，需要一个一个来获取的时候使用
3 attr(属性名)  获取想要的属性信息
4 text() 获取文本  只要文本，所有html标签全部被过滤
5 html(html数据)  获取html内包括html标签在内的全部内容  
'''
















