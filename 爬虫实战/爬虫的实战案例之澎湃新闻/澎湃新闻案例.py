import requests  # 导入requests模块
from bs4 import BeautifulSoup  # 导入bs4模块
import os  # 导入os模块是为了在爬取目标文本后进行保存
# 获取澎湃新闻的url
url = 'https://www.thepaper.cn/newsDetail_forward_26649723'
# 通过requests模块进行访问
obj = requests.get(url)
#print(obj.headers)  打印头部信息)
# print(obj)   <Response [200]> 请求成功
# print(obj.text)   接受澎湃新闻网页的文本内容
# 通过BeautifulSoup模块解析网页的文本信息
res = BeautifulSoup(obj.text,'html.parser')
'''
dates = res.find_all('p')
p标签内包括很多文本之外的内容所以要爬取指定的文本内容要先找到文本内容所在的div盒子在寻找p标签
'''
# 通过网页内鼠标右键检查网页寻找的装有文本内容的div盒子
div_dates=res.find('div',class_='index_cententWrap__Jv8jK')
# print(div_dates)
# 找到文本内容的div父类盒子之后开始寻找盒子内的p标签
p_dates=div_dates.find_all('p')
# print(p_dates)
# 如果当前路径下不存在名为p_dates的文件就运行if里面的代码
if not os.path.exists('p_dates'):
    # mkdir有创建文件的功能 os.mkdir()括号内为想要创建的文件名称  代码意为创建一个名字叫p_dates的文件
    os.mkdir('p_dates')
# 进行数据循环 进行文本的写入
for i in p_dates:
    # 循环的i就是每一个p标签要想去除前后的<p>标签就要打印p的文本内容
    # 获取文本内容
    #print(i.text)
    # 获取到文本内容之后通过 with open 进行写入信息  'p_dates/img.txt' 意为p_dates文件夹下的img文本
    with open('p_dates/img.txt','a',encoding='utf-8') as f:
        f.write(i.text+'\n')



# print(dates) 直接打印文本内容过于繁杂通过循环可以更清晰的查看爬取的文本内容
