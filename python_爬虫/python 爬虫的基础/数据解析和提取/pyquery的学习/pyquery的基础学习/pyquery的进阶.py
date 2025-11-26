from pyquery import PyQuery

html = """
<HTML>
    <div class='aaa'>哒哒哒</div>
    <div class='bbb'>嘟嘟嘟</div>
</HTML>
"""

p = PyQuery(html)

# 增加数据
# p('div.aaa').after("""<div class='ccc'>嘎嘎嘎</div>""")
# print(p)
'''
<HTML>
    <div class="aaa">哒哒哒</div>
    <div class="ccc">嘎嘎嘎</div><div class="bbb">嘟嘟嘟</div>
</HTML>
'''


# 增加文本数据
# p('div.aaa').append("""<span>我爱你</span>""")
# print(p)
'''
<HTML>
    <div class="aaa">哒哒哒<span>我爱你</span></div>
    <div class="bbb">嘟嘟嘟</div>
</HTML>
'''


# 修改属性
# p('div.bbb').attr('class','aaa')
# print(p)
'''
<HTML>
    <div class="aaa">哒哒哒</div>
    <div class="aaa">嘟嘟嘟</div>
</HTML>
'''


# 新增属性 前提是新增的标签内没有这个属性
# p('div.bbb').attr('id','10086')
# print(p)
'''
<HTML>
    <div class="aaa">哒哒哒</div>
    <div class="bbb" id="10086">嘟嘟嘟</div>
</HTML>
'''

# 删除标签
# p('div.bbb').remove()
# print(p)
'''
<HTML>
    <div class="aaa">哒哒哒</div>
    
</HTML>
'''
