import time

import requests
from lxml import etree
# 获取目标的url
url = 'https://www.zbj.com/fw/?k=%E7%BD%91%E7%AB%99%E5%BC%80%E5%8F%91&fr=pc_zbj_v2022-homepage'
# 获取到url数据后开始进行数据请求
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',
    'cookie':'_uq=ab12444344ae4bafba02555ada023b67; uniqid=d01pjrfk3err7; _suq=8188dbc8-7079-43bd-b99f-514a759d480d; oldvid=; vid=7cc3512f85d0b4fc78e4b8b4cbea2c8d; unionJsonOcpc=eyJvdXRyZWZlcmVyIjoiaHR0cHM6Ly9jbi5iaW5nLmNvbS8iLCJwbWNvZGUiOiIifQ==; local_city_path=wuhan; local_city_name=%E6%AD%A6%E6%B1%89; local_city_id=3627; nsid=s%3AMw53KiaSYwr3vCNW3muz_rPhIA5xac_p.Np%2Bg2pRWSkFOhwMtA%2BYdQUnXrA5ocWgqiqKILQ%2BfdNE; vidSended=1; Hm_lvt_a360b5a82a7c884376730fbdb8f73be2=1760577949,1760610672; HMACCOUNT=127DE6665E3ECEEB; Hm_lpvt_a360b5a82a7c884376730fbdb8f73be2=1760610678; s_s_c=xhA3dh7QsA2lgP8ro4tGRzKmv%2BbCrfNNrMc12G7nVOwGRMYB5NmkgWzr7yIF2wl9jXj0KMSfp2XBDG0XoAXBBQ%3D%3D'
}
resp = requests.get(url)
# 获取到页面数据之后开始进行数据的初始化
html = resp.text
# 导入xpath开始解析和筛选数据
et = etree.HTML(html)
# 想要找到整个页面的商品数据先要找到包含商品数据的div盒子 在从div盒子中循环数据开始进行数据的筛选
div_date = et.xpath('//div[@class="service-card-wrap"]/div')
# 进行数据的循环开始进行数据的提取
for i in div_date:
    print('-------------------')
    # print(i)
    # 确认div数据无误开始进行数据的筛选
    price = i.xpath('./div/div[@class="price"]/span/text()')
    obj_price = price[0]
    if not obj_price:
        continue
    # 商品价格爬取正确
    print(obj_price)
    time.sleep(1)

