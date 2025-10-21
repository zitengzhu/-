import requests
import re
import time

# 获取电影天堂的url
url = 'https://www.dytt8899.com/'
url_1 = 'https://www.dytt8899.com'
# 请求页面信息
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
    'cookie':'UM_distinctid=199e6082081581-06726fff85f27f-4c657b58-1bcab9-199e60820821a95; CNZZDATA1281410151=605239009-1760500916-%7C1760502164'
        }
resp = requests.get(url,headers=headers)
# 访问信息后发现打印去页面出现乱码需要解析器进行解析  解析器有  gbk 和 utf-8 两个
# 进行解析请求到的数据
resp.encoding='gbk'
# print(resp.text)
# 成功获取到正确的数据后开始寻找目标href的区域
# 编辑正则表达式
# 想看那个栏目的电影就把标题换一下就可以了
obj_1 = re.compile(r'2025必看热片.*?<ul>(?P<html>.*?)</ul>',re.S)
# 导入正则表达式 筛选数据
dates = obj_1.search(resp.text)
html = dates.group('html')
# print(res_1)
# 获取到目标区域后开始编写正则表达式寻找目标href数据
obj_2 = re.compile(r"<li><a href='(?P<href>.*?)' title")
# 导入正则筛选数据
res_2 = obj_2.finditer(html)
# 循环内容获取信息
for i in res_2:
    # print(i.group('href'))
    a = i.group('href')
    # 获取目标电影的url地址
    new_url = url_1+a
    # print(new_url)
    # 请求网页数据
    resp_1=requests.get(new_url)
    # 访问信息后发现打印去页面出现乱码需要解析器进行解析
    resp_1.encoding='gbk'
    # 页面解析完成开始编写正则表达式
    obj_3 = re.compile(r'<div class="title_all"><h1>(?P<name>.*?)</h1></div>.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)
    # 正则编写完毕开始进行信息的筛选
    res = obj_3.search(resp_1.text)
    name=res.group('name')
    download=res.group('download')
    print('电影名称:'+name)
    print('下载地址（下载地址需要冒号后面全部提取）:'+download)
    print('----------------------')
    time.sleep(1)

