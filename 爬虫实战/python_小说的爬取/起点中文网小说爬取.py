'''
1获取起点网站要爬取的小说的各个章节的url
2获取到章节url后进行保存
'''
import time
import os
import requests
from bs4 import BeautifulSoup

# 获取到了存在小说目录的url
url = 'https://www.qidian.com/book/1045238424/'
# 获取到路标数据存在的url后用requests模块进行请求
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
    'referer':'https://www.qidian.com/chapter/1045238424/846244349/',
    'cookie':'e2=%7B%22l6%22%3A%221%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A14%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22qd_G55%22%7D; e1=%7B%22l6%22%3A%221%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_xiangqing%22%2C%22eid%22%3A%22qd_H_mulublock%22%7D; waftest=1; abPolicies=%7B%22g2%22%3A1%2C%22g6%22%3A0%2C%22g4%22%3A0%2C%22g1%22%3A3%2C%22g5%22%3A0%2C%22g3%22%3A0%7D; supportwebp=true; newstatisticUUID=1760145121_16467995; _csrfToken=2EcptjNi7qApmc6gMR4DQg2NExpQoA2G1w0OkqfV; Hm_lvt_f00f67093ce2f38f215010b699629083=1760145122; HMACCOUNT=127DE6665E3ECEEB; fu=2040024146; e2=; e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A18%22%7D; supportWebp=true; abPolicy_3_1=3; traffic_search_engine=; se_ref=; traffic_utm_referer=https%3A%2F%2Fcn.bing.com%2F; Hm_lpvt_f00f67093ce2f38f215010b699629083=1760145190; w_tsfp=ltvuV0MF2utBvS0Q76rokUyoFT4ucTs4h0wpEaR0f5thQLErU5mD0Yd/uc3zNHXc4Mxnvd7DsZoyJTLYCJI3dwNHE8mWJtgSiAuRkdAkiYYUUhFgQpONCFdNcrlx7TNOLnhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5TyO7Vnzel8mCulK0kWT1XkeWC4i4BS4cLteYEitK8f9SqA='
}
res = requests.get(url,headers=headers)
# 数据请求到之后开始解析页面的文本数据
page_dates = BeautifulSoup(res.text,'html.parser')
# 分析完数据之后开始寻找保存目录的url
a_dates = page_dates.find_all('a',class_='chapter-name')
'''
for i ,a in enumerate(a_dates):
    data_cid = a['data-cid']
    print(data_cid)
    可以更快速的找到目标数据
'''
# url找到之后设置循环方便查看
for i in a_dates:
    # print(i)
    href = i['href']
    name = i['alt']
    # print(type(href)) <class 'str'>
    # 找到href地址后发现缺少协议部分 查看数据类型后发现是字符串 可以用字符串的拼接组成完整的url
    url_dates = 'https:'+href
    # 获取到了完整的url
    # print(name)
    # print(url_dates)
    # 获取到了每个章节的url之后用requests进行请求用来获取章节的内容
    img = requests.get(url_dates,headers=headers)
    # 请求到数据后开始解析网页
    img_dates = BeautifulSoup(img.text,'html.parser')
    time.sleep(2)
    # 查看解析后的内容发现文本存在在p标签内 寻找p标签过滤内容
    # p_dates = img_dates.find_all('p')
    p_dates = img_dates.find_all('p',class_=False)
    # 检查目标数据无误后利用os模块进行保存
    if not os.path.exists('小说'):
        os.mkdir('小说')
    # 找到文本数据之后设置循环方便查看文本数据
    for i in p_dates:
        # print(i.text)
        # 创建文件夹完成后开始用with open 进行保存  小说不属于视频 音频 图片的二进制数据
        with open (f'小说/明末：我带着两白旗反清怎么了？/{name}.txt','a',encoding='utf-8') as f:
            f.write(i.text+'\n')
    print(name,'下载完成')
    print('------------------------')
