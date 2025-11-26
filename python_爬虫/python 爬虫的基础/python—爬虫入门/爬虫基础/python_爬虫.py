# requests 是爬虫的外部模块
import time

import requests

# 发送get请求 主要用来获取服务器的数据
def get_url():
    # 1.定义要访问的url
    url='https://www.baidu.com/'
    # 2. 设置变量a接受爬虫模块(requests.get(url))所包含的数据
    # get是请求所以get后括号内放的是想求取的url的地址
    a=requests.get(url)
    print(a)  # <Response [200]> 出现200以为着代码运行成功
    print(a.text)  # 获取url地址对应的网页的文本信息
    print(a.status_code)  # 200  打印状态码
    print(a.headers)  # 打印头部信息
#get_url()
'---------------------------------------------------------------------------------------------'
# 发送post的请求 通常用于想服务器提交数据
def post_url():
    # 1.定义要提交的数据的url  ？后面的就是要提交的数据
    # 第一种提交数据的方法
    # url = 'https://www.baidu.com/?name=777'   name=777 就是要提交的数据
    # a = requests.post(url)
    # 第二种提交数据的方法 定义字典 通过字典的形式进行传参
    url = 'https://www.baidu.com/'
    canshu={'name':'zzt','psw':'20060914'}
    a=requests.post(url,data=canshu)
    # 打印 文本信息
    print(a.text)
    # 打印状态码
    print(a.status_code)
#post_url()

'-------------------------------------------------------------------------------------------------'

# 图片的下载
def download_url():
    # 想要通过爬虫下载图片就需要先获取图片的url地址
    url='https://steamcommunity.com/sharedfiles/filedetails/?id=3313405923'
    # 将想获取的图片的url信息存储在a这个变量中
    a=requests.get(url)
    # 操作图片必须要用到content 二进制
    print(a.content)
    with open('c.png','wb') as f:
        f.write(a.content)
# download_url()
'----------------------------------------------------------------------------------------------------'
'''
网页有两种：静态标签  动态标签
    静态标签：直接拿着url就可以获取数据
            在网页右键检查的时候发现目标数据在标签中 而且用requests模块爬取的时候也能获取到
    动态数据：不看浏览器上面的url地址
            看的是右键检查网络里面的fetch/xhr标签
可以优先用静态数据找 找不到换动态数据       
'''

'---------------------------------------------------------------------------------------------------------'

'''
 请求头 有 User-Agent  Referer  Cookie （在标头里面找）
具体格式为

headers={
'uesr-agent'='标头内对应的数据'
'referer'='标头内对应的数据'
'cookie'='标头内对应的数据'
}
'''

'------------------------------------------------------------------------------------------------------'


# 爬取百度的源代码的两种格式
'''
url='https://www.baidu.com/'
res=requests.get(url)
res.encoding='utf-8'
print(res.text)

url='https://www.baidu.com/'
date=requests.get(url)
dates=BeautifulSoup(date.text,'html.parser')
print(dates)
'''


'------------------------------------------------------------------------------------------------------'

# 查看python的请求头信息
'''
url = 'https://www.baidu.com/'
res = requests.get(url)
print(res.request.headers)
 请求头信息的详细数据 : {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
'''

'----------------------------------------------------------------------------------------------------------'
# 百度翻译传参--post请求的练习

# query = input('请输入你想翻译的英文单词')
# 通过date变量设置kw 设置需要翻译的单词
# date = {'kw':query}
# 添加请求头
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
         # 'referer':'https://fanyi.baidu.com/mtpe-individual/transText?query=dog%0A&lang=en2zh',
         # 'cookie':'BIDUPSID=5C4332580E18DEAEB3D506BD701D1398; PSTM=1758721189; BAIDUID=9F6D5A1102B3BEDEC7B6FFE499DD0FDC:FG=1; BAIDUID_BFESS=9F6D5A1102B3BEDEC7B6FFE499DD0FDC:FG=1; ZFY=KLdt4XUdAy:A0AveAGBZw:B3JWfHxlzWN8ot3RnZj9cak:C; H_WISE_SIDS=64752_64870_64833_64987_65133_65139_65194_65203_65224_65245_65255_65271_65280_65326_65367_65178_65454_65489_65503; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22199c2ff54e9144d-0aecaf953edbd48-4c657b58-1821369-199c2ff54ea24d8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk5YzJmZjU0ZTkxNDRkLTBhZWNhZjk1M2VkYmQ0OC00YzY1N2I1OC0xODIxMzY5LTE5OWMyZmY1NGVhMjRkOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; in_source_business=01007; H_PS_PSSID=64987_65133_65194_65224_65245_65255_65271_65280_65367_65178_65454_65462_65511_65543_65596_65621_65628_65634_65476_65662_65678_65670_65689; BA_HECTOR=0000aha52h0g2g0ga18k00a5058h0m1kekshh24; AIT_PERSONAL_VERSION=1; AIT_ENTERPRISE_VERSION=1; ab_sr=1.0.1_YTExZWViOTkyNzcxYTkxYTk4ZDNhMDhiZDkwODAyMmYwMmJiODI5M2QwYTc0ZTg1YjI3YTE1NTc5M2M1NDI0ZGE3NzliYTBkNzE3MDg0ZjdhMGViMjkxYzQ3Yjc0OWRmNjUwNGUxMWI4OTM5YzY4ODM5ZjA5ZjhhMTE5YTRkZWNlZDg3NmIxMjM4YWYyNWFkYzdmMTUwZGYyNDE0NzZkMg==; RT="z=1&dm=baidu.com&si=0bb32159-bfa7-497c-8a81-57835776d239&ss=mgn1n3tv&sl=9&tt=9g3&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=9dhb"'
# }
# url = 'https://fanyi.baidu.com/sug'
# 上传需要翻译的数据
# tra = requests.post(url,data=date,headers=headers)
# 数据为字典属于json类型
# print(tra.json()['data'])
# dates = tra.json()['data']
# for i in dates:
    # print(i['v'])


'-----------------------------------------------------------------------------------------------------------'
# 多个参数的get请求的处理


# 第一种直接在标头内复制
url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=20'


# 第二种进行url的拼接
url_1 = 'https://movie.douban.com/j/chart/top_list'
date = {'type':'6','interval_id':'100:90','action':'','start':'0','limit':'20'}
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0x-requested-withXMLHttpRequest',
    'referer':'https://movie.douban.com/typerank?type_name=%E6%83%85%E8%89%B2&type=6&interval_id=100:90&action=',
    'cookie':'l="118254"; bid=G_XCGTek99I; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1760236212%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.4cf6=f99b27e7ad132d76.1760236212.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.402924764.1760236212.1760236212.1760236212.1; __utmb=30149280.0.10.1760236212; __utmc=30149280; __utmz=30149280.1760236212.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.333804266.1760236212.1760236212.1760236212.1; __utmb=223695111.0.10.1760236212; __utmc=223695111; __utmz=223695111.1760236212.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=LJvOCpjC6HsPmtuBlAtLFsccFmB27los; _vwo_uuid_v2=DE3E3AA15588C362A177B41650506858B|5cc30aae0b03f2d017eee780e77aea7a'}
response = requests.get(url,params=date,headers=headers)
# print(response.request.url)
# https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=20&type=6&interval_id=100%3A90&action=&start=0&limit=20


# 下方多行注释为爬取的电影具体信息
'''
# print(response.json())
dates = response.json()
for i in dates:
    print('-------------')
    # print(i)
    name=i['title']
    print('名称:'+str(name))
    regions=i['regions']
    print('国家:'+str(regions))
    actors=i['actors']
    print('演员:'+str(actors))
    release_date=i['release_date']
    print('上映时间:'+str(release_date))
    types=i['types']
    print('类型:'+str(types))
    movie=i['cover_url']
    print('电影播放路径:'+movie)
    time.sleep(1)
'''

'--------------------------------------------------------------------------------------'





























