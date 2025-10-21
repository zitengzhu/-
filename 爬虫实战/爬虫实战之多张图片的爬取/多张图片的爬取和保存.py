import time
import requests
from bs4 import BeautifulSoup
import os
# 找到要爬取网站的url地址
stare_page=int(input('请输入开始爬取的页数'))
end_page=int(input('请输入结束爬取的页数'))
for i in range(stare_page,end_page+1):
    url=f'https://haowallpaper.com/?page={i}&sortType=3&wpType=1&rows=9&isFavorites=false&typeId=35c203f75643ac7803b8f706fa91ef40'
    # 找到目标的url地址之后用request模块进行请求
    dates = requests.get(url)
    # 请求到内容之后用bs4模块进行页面文本内容分析
    res = BeautifulSoup(dates.text,'html.parser')
    # 分析完成之后用find_all去寻找所有图片的div盒(每一个图片都存在与一个div盒子中
    div_dates = res.find_all('div',class_='card')
    # 通过find_all获取了大量数据 通过循环降低信息的辨别难度
    for i in div_dates:
        # i 是每一个div盒子的循环 图片存在于div盒子中
        # 通过find找到img 用来获取src地址和图片的名称方便保存
        print('----------------------------------------')
        img = i.find('img')
        img_src = img['src']  # 每张图片的url地址
        img_name = img['alt']  # 每张图片的名称
        # print(img_src)
        # print(img_name)
        # 获取了图片的url地址和名称之后就可以进行批量保存了
        # 通过 requests 模块请求每张图片的数据
        picture = requests.get(img_src)
        # 通过os模块创建文件来保存爬取到的图片
        if not os.path.exists('picture'):
            os.mkdir('picture')
            # 在picture文件夹下存放下载的照片
        with open(f'picture/{img_name}.png','wb') as f:
            # 图片为二进制内容 (相关信息请查看爬虫基础中的数据保存.py文件)
            f.write(picture.content)
            print(f'{img_name}已经下载成功')
            # 爬虫为代码模仿人的行为所以在爬取是应适当的停顿代码用来防止网站识别
            time.sleep(1)