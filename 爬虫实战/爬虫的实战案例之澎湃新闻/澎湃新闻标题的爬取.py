import requests  # 导入requests模块
from bs4 import BeautifulSoup  # 导入bs4模块
import os
import os  # 导入os模块是为了在爬取目标文本后进行保存
# 获取澎湃新闻的url
url = 'https://www.thepaper.cn/newsDetail_forward_26649723'
# 通过requests模块进行访问
obj = requests.get(url)
# 获取到url地址后开始用BeautifulSoup进行分析
dates=BeautifulSoup(obj.text,'html.parser')
# 分析之后想要获取澎湃新闻的标题 先要找到装有新闻标题的div盒子
div_dates=dates.find('div',class_='index_wrapper__L_zqV')
# 找到标题所在的div盒子之后开始寻找标题所在的位置
title_dates=div_dates.find(class_='index_title__B8mhI')
# 标题所对应的位置之后读取对应的文本来获取标题
#print(title_dates.text)
with open('p_dates/title.txt','w',encoding='utf-8') as f :
    f.write(title_dates.text)
