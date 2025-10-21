import time
import requests
import re
import os
# 豆瓣电影TOP250的url数据
page=input('请输入你想打印的页数')
url = f'https://movie.douban.com/top250?start={(int(page)-1)*25}&filter='
# 设置请求头
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
    'referer':'https://cn.bing.com/',
    'cookie':'ll="118254"; bid=G_XCGTek99I; _pk_id.100001.4cf6=f99b27e7ad132d76.1760236212.; __yadk_uid=LJvOCpjC6HsPmtuBlAtLFsccFmB27los; _vwo_uuid_v2=DE3E3AA15588C362A177B41650506858B|5cc30aae0b03f2d017eee780e77aea7a; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1760410508%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.402924764.1760236212.1760236212.1760410508.2; __utmb=30149280.0.10.1760410508; __utmc=30149280; __utmz=30149280.1760410508.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.333804266.1760236212.1760236212.1760410508.2; __utmb=223695111.0.10.1760410508; __utmc=223695111; __utmz=223695111.1760410508.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/'
}
# 设置变量获取请求到的信息
res = requests.get(url,headers=headers)
# res = requests.get('https://movie.douban.com/top250') 效果和第12行一样
# 设置变量承接 请求到的页面数据
obj = res.text
# 设置正则表达式 筛选页面信息
# re.S 可以让正则中的点匹配换行符
formula = re.compile(r'<div class="item">.*?<a href="(?P<herf>.*?)".*?<span class="title">(?P<name>.*?)</span>.*?<div class="bd">.*?<p>.*?导演:(?P<dao>.*?)&nbsp.*?<br>(?P<year>.*?)&nbsp;/&nbsp;(?P<dress>.*?)&nbsp;/&nbsp;(?P<leixing>.*?)</p>.*?<span>(?P<number>.*?)人评价</span>.*?<p class="quote">.*?<span>(?P<pinglun>.*?)</span>',re.S)
# 设置变量接收 迭代器的数据
result = formula.finditer(obj)
# 循环迭代器获取数据
for i in result:
    name = i.group('name')
    dao = i.group('dao')
    year = i.group('year').replace(' ','')
    dress = i.group('dress')
    leixing = i.group('leixing')
    number = i.group('number')
    pinglun = i.group('pinglun')
    # 拿到了页面的url可以开始爬取主演的信息了
    print('-----------------------------------')
    print('电影名称:'+name)
    print('导演:'+dao)
    print('上映年份'+year)
    print('国家:'+dress)
    print('类型:'+leixing)
    print('评论人数:'+number)
    print('评语:'+pinglun)
    time.sleep(1)

