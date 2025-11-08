from lxml import etree

# xpath的位置从一开始数

# 练习为XML
xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id='10086'>周大强</nick>
        <nick id='10010'>周芷若</nick>
        <nick class='joy'>周杰伦</nick>
        <nick class='jolin'>蔡依林</nick>
        <div>
            <nick>惹了</nick>
        </div>
    </author>
    <partner>
        <nick id='ppc'>胖胖陈</nick>
        <nick id='ppbc'>胖胖不陈</nick>
    </partner>
</book>
"""

# 解析xml
et = etree.XML(xml)
# result = et.xpath('/book')  # /表示根节点
# print(result)  [<Element book at 0x1b18a3d0c00>]  找到了 book 节点

# result = et.xpath('/book/name')   找book里面的name子节点
# print(result)  [<Element name at 0x29ea3072d40>]

# result = et.xpath('/book/name/text()') text()可以找到文本内容
# print(result)  ['野花遍地香']
# xpath 默认返回的是列表可以根据列表的查找去掉括号
# result = et.xpath('/book/name/text()')[0]
# print(result)  野花遍地香
'''
xpath的数据查找方式与文件路径类似 从父节点到子节点的逐层寻找
'''

# //可以寻找所有的目标子节点
'''
result = et.xpath('/book//nick')
print(result)
[<Element nick at 0x17c225e2d40>, <Element nick at 0x17c225e2f00>, <Element nick at 0x17c225e3340>, <Element nick at 0x17c225e30c0>,
 <Element nick at 0x17c225e3040>, <Element nick at 0x17c225e3280>, <Element nick at 0x17c225e3240>, <Element nick at 0x17c225e3080>]
'''

# *号表示任意节点  是通配符号
'''
result = et.xpath('/book/*/nick')
print(result)
[<Element nick at 0x2c6bd792d40>, <Element nick at 0x2c6bd792f00>, <Element nick at 0x2c6bd793340>,
 <Element nick at 0x2c6bd7930c0>, <Element nick at 0x2c6bd793040>, <Element nick at 0x2c6bd793280>]
'''


#   [@属性名='值']可以查找符合节点属性的数据
# result = et.xpath('/book/author/nick[@class="joy"]/text()')
# print(result)      ['周杰伦']



# @id 可以拿到id值
result = et.xpath('/book/author/nick/@id')
# print(result)   ['10086', '10010']



'----------------------------------------------------------------------------------------------------------'
# html
html = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='utf-8'>
    <title>Title</title>
</head>
<body>
    <ul>
        <li><a href='http://www.baidu.com'>百度</a></li>
        <li><a href='http://www.google.com'>谷歌</a></li>
        <li><a href='http://www.sogou.com'>搜狗</a></li>
    </ul>
    <ol>
        <li><a href='feiji'>飞机</a></li>
        <li><a href='dapao'>大炮</a></li>
        <li><a href='huoche'>火车</a></li>
    </ol>
    <div class='job'>李嘉诚</div>
    <div class='common'>胡辣汤</div>
</body>
</html>    
"""
# 加载xpath
et = etree.HTML(html)

# html的li子节点打印出来是一个包括三个数据的列表 通过在li后面加[]通过列表索引具体的数据
# li_list = et.xpath('/html/body/ul/li[2]/a/text()')
# print(li_list)   ['谷歌']

# 可以通过//寻找所有的子节点
li_list = et.xpath('//li')
for i in li_list:
    date = i.xpath('./a')  # ./表示的是当前节点  代码意为 在 li 这个当前标签中寻找a标签
    href = i.xpath('./a/@href')[0]  # 寻找a标签的href数据
    text = i.xpath('./a/text()')[0]  # 寻找a标签的text数据
    print(text,href)

