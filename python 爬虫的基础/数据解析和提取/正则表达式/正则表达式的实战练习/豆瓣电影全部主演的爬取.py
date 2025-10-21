import time
import requests
import re
import os
from bs4 import BeautifulSoup
# 豆瓣电影TOP250的url数据
url = 'https://movie.douban.com/top250'
# 设置请求头
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
    'referer':'https://cn.bing.com/',
    'cookie':'ll="118254"; bid=G_XCGTek99I; _pk_id.100001.4cf6=f99b27e7ad132d76.1760236212.; __yadk_uid=LJvOCpjC6HsPmtuBlAtLFsccFmB27los; _vwo_uuid_v2=DE3E3AA15588C362A177B41650506858B|5cc30aae0b03f2d017eee780e77aea7a; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1760410508%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.402924764.1760236212.1760236212.1760410508.2; __utmb=30149280.0.10.1760410508; __utmc=30149280; __utmz=30149280.1760410508.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.333804266.1760236212.1760236212.1760410508.2; __utmb=223695111.0.10.1760410508; __utmc=223695111; __utmz=223695111.1760410508.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/'
}
res = requests.get(url,headers=headers)
obj=re.compile(r'<div class="item">.*?<a href="(?P<href>.*?)".*?</span>',re.S)
dates=obj.finditer(res.text)
for i in dates:
    # print(i['href'])
    a=i['href']
    # 获取到了目标的url开始请求数据
    header={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
        'cookie':'_TDID_CK=1760500425941; 6333762c95037d16=Y3MBd2v6Wj5Q1JoGML6AEUWy2qOURgLuDAMwGnjQAEEXn3OJu%2BLH0Or3jq%2BNh9Oh5Qhs4rRHlBId3NIEQI36aTKOTMwBfLzyUu82gAA5%2FRLinH1wf%2FafJwlQqza0aiZLZlaZAkmQ1A71Rzr1oETvhdhNoJulB96%2BDztRNmDkOulmU63AywYoGa%2BIiTcs3SW%2BvbMe3ozMrhRUwHuA2fOSqqzdAsSe89%2FafzaP%2FTaTn5axl%2FGFob%2FfUEBqExuztQTSt37dZ2yGFzUnhp0exIHaWAl0REN1UAWT0EfkmRhRImLsjgoVosv1NA%3D%3D; ll="118254"; bid=G_XCGTek99I; _pk_id.100001.4cf6=f99b27e7ad132d76.1760236212.; __yadk_uid=LJvOCpjC6HsPmtuBlAtLFsccFmB27los; _vwo_uuid_v2=DE3E3AA15588C362A177B41650506858B|5cc30aae0b03f2d017eee780e77aea7a; __utmz=30149280.1760410508.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1760410508.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1760500350%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.402924764.1760236212.1760438946.1760500350.7; __utmb=30149280.0.10.1760500350; __utma=223695111.333804266.1760236212.1760438946.1760500350.7; __utmb=223695111.0.10.1760500350; __utmc=30149280; __utmc=223695111'
    }
    b=requests.get(a,headers=header)
    c=b.text
    d=BeautifulSoup(c,'html.parser')
    print(d)
    # 学习html相关的内容



