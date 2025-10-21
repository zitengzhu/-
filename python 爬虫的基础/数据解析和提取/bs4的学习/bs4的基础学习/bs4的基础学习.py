from bs4 import BeautifulSoup

html = """
<ul>
    <li><a href="zhangwuji.com">张无忌</a></li>
    <li><a href="zhubajie.com">猪八戒</a></li>
    <li><a href="wuzetian.com">武则天</a></li>
    <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
</ul>
"""
# 获取到页面数据后第一步是用 BeautifulSoup 模块解析网页
resp = BeautifulSoup(html,'html.parser')

# resp.find('标签名',attrs={'属性':'值'})       查找页面内的特定元素，只会有一个结果
dates = resp.find('li',attrs={'id':'abc'})
'''
dates = resp.find('li',id='abc')
dates = resp.find('li',attrs={'id':'abc'})
两者效果相同
'''
# print(dates)      <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
# 通过.txt可以获得代码内的文本信息
# print(dates.text)  周星驰
# 找到目标数据后依旧可以通过find再次筛选数据
res = dates.find('a')
# print(res)                 <a href="zhouxingchi.com">周星驰</a>
# 通过.get() 可以进一步筛选想要的信息
# print(res.get('href'))     zhouxingchi.com

# resp.find_all('标签名',attrs={'属性':'值'})   查找目标数据内所有符合要求的值
dates_1 = resp.find_all('li')
# 设置循环 让打印的数据更方便查看
for i in dates_1:
    # print(i)
    # 找到目标数据后可以通过 find 再次筛选
    obj = i.find('a')
    # print(obj)
    name = obj.text
    href = obj.get('href')
    # print(name,href)





