'''
1获取起点网站要爬取的小说的各个章节的url
2获取到章节url后进行保存
'''
import time
import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.qidian.com/book/1045238424/'
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
    # print(type(name))   <class 'str'>
    time.sleep(1)
    # 字符串的切割找到章节数字   1-9第十七个字符  10-99第十七到十八个字符    100-n第十七到第十九个字符
    # 通过判断字符大小索引数字///
    # 索引一位数页数
    # page=name[17]
    # 索引两位数页数
    # page = name[17:19]
    # 索引三位数页数
    # page = name[17:20]
    # print(page)
# 小说保存是出现章节顺序混乱  加入if判断 进行  明末：我带着两白旗反清怎么了？/{name}.txt' 的章节  第一章 第二章  第三章 ////
# 出现的问题 如何进行章节数字大小的判断
# 第 n-1 章 =<第 n 章
# 第n-1章
# 第n章
'''
if f'明末：我带着两白旗反清怎么了？第{}章':
    
'''