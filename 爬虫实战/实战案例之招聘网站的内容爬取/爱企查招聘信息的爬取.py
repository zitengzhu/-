# 找到爱企查网页的url地址
# 进入网页后寻找有关招聘信息的div盒子
# 在div盒子中查到关于招聘信息的内容并进行爬取
# 将爬取到的内容进行保存

import requests
from bs4 import BeautifulSoup
stare_time=int(input('请输入开始的页数'))
end_time=int(input('请输入结束的页数'))
for i in range(stare_time,end_time+1):
    # 找到网页对应的url
    url = f'https://yiqifu.baidu.com/g/aqc/joblist/getDataAjax?q=python&page={i}&district=100000&salaryrange='
    # 制作请求头    请求头详细信息请查看python爬虫的基础/python_爬虫.py
    headers={
        'cookie':'BIDUPSID=5C4332580E18DEAEB3D506BD701D1398; PSTM=1758721189; BAIDUID=9F6D5A1102B3BEDEC7B6FFE499DD0FDC:FG=1; BAIDUID_BFESS=9F6D5A1102B3BEDEC7B6FFE499DD0FDC:FG=1; ZFY=KLdt4XUdAy:A0AveAGBZw:B3JWfHxlzWN8ot3RnZj9cak:C; H_WISE_SIDS=64752_64870_64833_64987_65133_65139_65194_65203_65224_65245_65255_65271_65280_65326_65367_65178_65454_65489_65503; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22199c2ff54e9144d-0aecaf953edbd48-4c657b58-1821369-199c2ff54ea24d8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk5YzJmZjU0ZTkxNDRkLTBhZWNhZjk1M2VkYmQ0OC00YzY1N2I1OC0xODIxMzY5LTE5OWMyZmY1NGVhMjRkOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; in_source_business=0105; in_source=; log_first_time=1759965371942; ppfuid=FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD8JYsoLTpBiaCXhLqvzbzmvy3SeAW17tKgNq/Xx+RgOdb8TWCFe62MVrDTY6lMf2GrfqL8c87KLF2qFER3obJGmVXQmqM6seEAgB/LlOs0+zGEimjy3MrXEpSuItnI4KDwxAMUTOS16BfoXMcd2lpC/2p1N6CkMY1aSnXgB1lGFteVpNGJfrvhCFoYVviHeBxTPT8gtJS5rrQgC8adbUyRXGgLbz7OSojK1zRbqBESR5Pdk2R9IA3lxxOVzA+Iw1TWLSgWjlFVG9Xmh1+20oPSbrzvDjYtVPmZ+9/6evcXmhcO1Y58MgLozKnaQIaLfWRMWxg8jAkEPs+b09272wkCcMJmBV3DqpyTuzDwSUDbMyyfzO9u0S9v0HHkJ/i4zKsdnTNS/pLMWceus0e757/UMRBb1xGl5gB30/31IHrnZ9AAv3LCf1Y7/fHL3PTSf9vid/u2VLX4h1nBtx8EF07eCMhWVv+2qjbPV7ZhXk3reaWRFEeso3s/Kc9n/UXtUfNU1sHiCdbrCW5yYsuSM9SPGDZsl7FhTAKw7qIu38vFZiq+DRc8Vbf7jOiN9xPe0lOdZHUhGHZ82rL5jTCsILwcRVCndrarbwmu7G154MpYiKmTXZkqV7Alo4QZzicdyMbWvwvmR2/m//YVTM8qeZWgDSHjDmtehgLWM45zARbPujeqU0T92Gmgs89l2htrSKIcyLHvvlKerNaBcdhzDl3A35IaZk6tlkK1JLuZx2npqf1QPKbPm9E9wacrGwTwm2VZdImdyxYIjA1uSy2hfTFv/d3cnXH4nh+maaicAPllDg5eQg3PzwS3cxyDdVnXm0S3SzlDBMoJre+/eEVILl9qcvBS4d56lzr3mG54TfQtVwLcpEpFKmqip0pBULmGPyA4GZbJZF2cdnYPJr70FQi7jkHNGy4rHPin1m+4ZUWd+8U/DHdNp0WOpGUbl3SfdQzQaYXvleBbteLbUi5NoCAChP5oZfoCeoKKuvUEAPXXTPVjO0TTi0sVqFSdG+GFyi03wlrm3wCRN8QsWhT10pXJL0RhcLTagDnxauF9flnVwi9Ab2aMyW4+YH1VZWIUhb3tLvNHPTHkHFSp+jk/nvSIqm2QKY6eaGrGin5tWA6V16uqFuBSz8I0Kfe0QZwk5OQXJfXuUV5r5wqrSluAqvgDLzQ2GA5eh8aiV0nDOGmtfhiYNjbs2NxP0acAgApNd0ew==; clue_site=pc; log_guid=45d133950b3a5b71e5a2738336f33222; log_chanel=; Hm_lvt_37e1bd75d9c0b74f7b4a8ba07566c281=1759965543; HMACCOUNT=127DE6665E3ECEEB; H_PS_PSSID=64752_64987_65133_65194_65224_65245_65255_65271_65280_65367_65178_65454_65489_65503_65462_65477_65511_65543; BA_HECTOR=8k8ga12004ak84802hal0l0080210l1kedsl925; PSINO=7; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; polaris_local_area=100000; ab_sr=1.0.1_NzEzOTlkNDdiYjc3ZWI2MTJlZDg5Y2E4YzUxNGZkZmEwY2Y4OWRiNmVkZjhjOTc1YjBmMzdkODNhYjE5OTMyNzJiMzE3N2U1MGIwYjhjODA4NTcxNmM1MzFkMTM3NGM3ZjUxNWIyZTBkY2Q3OGQ4MzJjMDg2OGU4MmYyODBhMGYyMTYyMGZkOGVjNmVjYmUyMjcyYmQzMDcwOWFlYzZjYg==; RT="z=1&dm=baidu.com&si=0bb32159-bfa7-497c-8a81-57835776d239&ss=mgilxvpx&sl=u&tt=hsu&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=e20v&ul=e4hy&hd=e4i2"; Hm_lpvt_37e1bd75d9c0b74f7b4a8ba07566c281=1759966033; log_last_time=1759966171783',
        'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
        'referer':'https://yiqifu.baidu.com/g/aqc/joblist?q=python'
    }
    # 通过requests模块获取网页数据  访问是加上请求头信息
    res = requests.get(url,headers=headers)
    # print(res.json()) # {'status': -1, 'msg': '非法请求', 'data': None} 遇到这种情况需要加上请求头信息模拟浏览器的操作
    # 接受数据  dates是i
    # dates = res.json()
    # 循环数据方便查看   i值循环后是字典中的键 想获取数据所对应的值要调用键
    '''
    for i in dates['data']['list']:
        print('--------')
        #print(i)
        # i打印出来后为字典 调用字典中的值要用键
        # 工作名称
        name = i['jobName'].replace('<em>','').replace('</em>','')
        print(name)
        # 工作薪资
        money = i['salary']
        print(money)
        # 公司
        company = i['company']
        print(company)
        # 城市
        city = i['city']
        print(city)
        # 学历
        education = i['edu']
        print(education)
        # 工作经验
        exp = i['exp']
        print(exp)
        # 招聘网站
        print(i['source'])
        # 为了获取详细的职位要求需要用 标头url中的bid和jobId
        job_id = i['jobId']
        b_id = i['bid']
        img_url = f'https://yiqifu.baidu.com/g/aqc/jobDetailAjax?jobId={job_id}&bid={b_id}'
        obj = requests.get(img_url,headers=headers)
        require = obj.json()
        print(require["data"]["desc"])
        '''

