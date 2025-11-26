import time

import requests
from bs4 import BeautifulSoup
import os
# 获取目标网址的url
url = 'https://www.umeituku.com/bizhitupian/meinvbizhi/'
# 获取到网页的url后开始进行数据的请求
resp = requests.get(url)
# 打印后发现出现乱码用解析器开始进行解析
resp.encoding='utf-8'
# print(resp.text)
# 成功获取到数据后用BeautifulSoup开始进行页面的解析
res = BeautifulSoup(resp.text,'html.parser')
# 解析完成后开始寻找目标href的div盒子
div_dates = res.find('div', class_='TypeList')
# 找到目标的div盒子后开始寻找href的具体数据
a_dates = div_dates.find_all('a',class_="TypeBigPics")
# print(a_dates)
# 设置循环方便查找数据
for i in a_dates:
    # print('---------------------------')
    # 找到了存在图片的href后开始进行出去提取
    href = i.get('href')
    # print(href)
    # 获取到正确的href地址后开始进行图篇数据的请求
    img = requests.get(href)
    img.encoding='utf-8'
    # print(img.text)
    # 获取到数据后开始解析
    obj = BeautifulSoup(img.text,'html.parser')
    # print(obj)
    name = obj.find('title').text
    # 请求到信息后开始进行保存
    if not os.path.exists('图片'):
        os.mkdir('图片')
    # 用来保存图片的文件夹创建好后开始进行图片保存
    with open(f'图片/{name}.jpg','wb') as f:
        f.write(img.content)
        print(f'{name}'+'已经下载完成')
        print('-------------')
        time.sleep(1)