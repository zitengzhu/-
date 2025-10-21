'''
1 获取网易云音乐爬取目标的url
2 找到url之后进行页面分析
3分析信息进行过滤找到目标信息
4 将爬取的信息进行保存
http://music.163.com/song/media/outer/url?id=ID数字.mp3
'''
import time
import requests
from bs4 import BeautifulSoup
import os
# 网易云音乐数据目标的url
url = 'https://music.163.com/discover/toplist?id=19723756'
# 获取到目标url之后进行获取页面数据
# print(res.text)  代码运行后发现爬取的数据缺失可以加上请求头信息来解决
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
           'referer':'https://music.163.com/',
           'cookie':'JSESSIONID-WYYY=xk08Iy5JDkotmbZpBJvnZpk6rduSMmOPgMU2m6UmcpmJY8vZ8JX9F2zqRnekGpbTQo5Do2eJswesPx4dTKEK9%5CUTq%2B0kOYUEj2Z7Z0bcOJ3vAY1M8eD2%2FnIvs%2Bk1c3w5o%5CAAQQo2PBzd6KiBKUcI9d1%2BW8%5CwiFiAJ3E5uw9AMJR%5Crvam%3A1760141072763; _iuqxldmzr_=32; _ntes_nnid=b38a451994bf47f1546b9e6ef6ea1615,1760139272796; _ntes_nuid=b38a451994bf47f1546b9e6ef6ea1615; NMTID=00OqUHoc0BsRQWoSkuaiU1kCGJCalsAAAGZ0HnlnA; WEVNSM=1.0.0; WNMCID=zjflbs.1760139273084.01.0; WM_NI=s4GSoCRHzsfGB%2Bxf68Bc6yy0EdPJ6SgVCmV6z7Gv4IMILo%2FkCj73DNWn2JzOhG4%2BqZpOgWOYbq9OAblJCFOXG0SpThQKdzw5z6U7unWE2vGaDUpgzjjflwXLz1yWhVw8TXk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb7ce80ac99aabad27d8b968ab7c15e969a9bb1c23cedbc8bb1b76efcb6b6a7f32af0fea7c3b92ab1ec89b4ee499298b694e54d82f5b887b53482bdfa9afc3c87bca0abb559a58a8d8ed53ebae98997b7438f978490ae6181b6f9d4c74695b2feabf945ac99fcccf452b491a9b8ce53a2aff7b0c46ab0968da7ce5485f09d91d7649395ac9bf63fbaea9bd8f866959bfe97c66b888bc088f962aabaa498db48baefb7b8eb5eb5e89cb9ea37e2a3; WM_TID=MKpuURrAcplFUFRQUROChrIQbpasyyA5; ntes_utid=tid._.kx29bS44XvtEQ0BUUFPT06MVO8L4so7l._.0; sDeviceId=YD-d4KiiFmgFJtBElVAFEKTkrJBf9fp58u0'
           }
res = requests.get(url,headers=headers)
# print(res.text)
# 数据获取完毕用bs4模块进行分析
obj = BeautifulSoup(res.text,'html.parser')
# 打印页面数据之后发现要爬取的目标都存在在a标签中 通过查询a标签来过滤信息获取目标数据
# a_dates = obj.find_all('a')
# 在初次过滤之后发现 数据没有过滤充分 目标数据中存在href数据可以用href=Ture进行二次过滤
a_dates = obj.find_all('a',href=True)
# 设置循环方便观察数据
for i in a_dates:
    # print(i)
    # 设置循环之后 i 打印出来默认为字典可以通过调用键的方式获取href值
    dates = i['href']
    # print(href)
# 过滤后发现数据依旧没有过滤干净可以通过if条件进行三次过滤 (if判断的条件必须为目标数据所拥有的普遍特征  /song?id=是本次爬取数据所共有的普遍特征)
    if '/song?id=' in dates and '$' not in dates:
        #print(dates)
        # print(type(dates)) <class 'str'>
        # 打印后发现本次数据充分过滤但数据缺少协议部分 数据的类型为字符串 可以用字符串的切割来获取目标
        id = dates[9:]
        # print(i.text)
        name = i.text
        # 获得数据的id
        # print(id)
        # 完整的id和音乐名称数据已经获取成功可以开始下载了
        # 下载歌曲需要外链
        url_music = f"https://music.163.com/song/media/outer/url?id={id}.mp3"
        # 外链的url设置好之后需要再次用requests模块进行访问
        music_res = requests.get(url_music)
        # 数据获取完毕通过os模块创建文件夹来保存数据
        if not os.path.exists('音乐'):
            os.mkdir('音乐')
            # 文件夹创建好之后用 with open 模块进行保存
        with open(f'音乐/{name}.mp3','wb') as f :
            f.write(music_res.content)
            print(name,'已下载----------------------')
            time.sleep(2)






