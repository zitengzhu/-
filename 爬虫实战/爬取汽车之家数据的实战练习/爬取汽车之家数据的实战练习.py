import time

import requests



def a():
    scoreList = [{'name': '空间', 'value': '4'}, {'name': '驾驶感受', 'value': '4'}, {'name': '油耗', 'value': '4'}, {'name': '外观', 'value': '4'}, {'name': '内饰', 'value': '5'}, {'name': '性价比', 'value': '4'}, {'name': '配置', 'value': '5'}]
    print(scoreList[0]['name'],scoreList[0]['value'])
    print(scoreList[1]['name'],scoreList[1]['value'])
    print(scoreList[2]['name'], scoreList[2]['value'])
    print(scoreList[3]['name'], scoreList[3]['value'])
    print(scoreList[4]['name'], scoreList[4]['value'])
    print(scoreList[5]['name'], scoreList[5]['value'])
    print(scoreList[6]['name'],scoreList[6]['value'])








star_page = int(input('请输入你开始爬取的页数'))
end_page = int(input('请输入结束爬取的页数'))
for i in range(star_page,end_page+1):
    url = f'https://koubeiipv6.app.autohome.com.cn/pc/series/list?pm=3&seriesId=65&pageIndex={i}&pageSize=20&yearid=0&ge=0&seriesSummaryKey=0&order=0'
    html = requests.get(url)
    html.encoding = 'utf-8'
    dates = html.json()
    for i in dates['result']['list']:
        print('---------------')
        # 车名
        name = i['carname']
        # 型号
        specname = i['specname']
        # 公里数
        distance = i['distance']
        # 价格
        buyprice = i['buyprice']
        # 购买地
        buyplace = i['buyplace']
        # 购买日期
        boughtDate = i['boughtDate']
        # 具体地点
        dealerName = i['dealerName']
        #居住地
        location = i['location']
        # 综合评分
        averageScore = i['averageScore']
        # 总结
        feeling_summary =i['feeling_summary']
        print('车名:'+name,'型号:'+specname)
        print('公里数:'+distance)
        print('价格:'+buyprice)
        print('购买地:'+buyplace)
        print('购买日期:'+boughtDate)
        print('具体地点:'+dealerName)
        print('居住地:'+location)
        print('综合评分:'+str(averageScore))
        a()
        print('总结:'+feeling_summary)
        time.sleep(1)