'''
案例：
    烤地瓜案例

需求：
    1.定义地瓜类 -> SweetPotato
    2.属性： 被烤时间 cook_time   地瓜状态 cook_state  调料 condiments
    3.行为： 烘烤 cook()  添加调料 add_condiments()
    4. 获取地瓜数据
    5.要求
    烘烤时间     地瓜状态
    [0,3)        生的
    [3,7)        半生不熟
    [7,12)        熟的
    [12,∞)        糊了
'''

# 定义地瓜类
class SweetPotato:
    def __init__(self):
        self.cook_time=0
        self.cook_state='生的'
        self.condiments=[]

    def cook(self,time):
        if time<=0:
            print('非法值')
        else:
            self.cook_time = time+self.cook_time
            if 0<self.cook_time<3:
                self.cook_state='地瓜是生的'
            elif 3 <= self.cook_time < 7:
                self.cook_state='地瓜半生不熟'
            elif 7 <= self.cook_time<12:
                self.cook_state ='地瓜熟了'
            else:
                self.cook_state ='地瓜糊了'
    def add_condiments(self,condiments):
        self.condiments.append(condiments)
    def __str__(self):
        return f'烘烤时间：{self.cook_time}  地瓜状态：{self.cook_state}  调料：{self.condiments}'

sp = SweetPotato()
# 烘烤时间
sp.cook(8)  # 8为给cook中time变量的定义值
# 添加调料
sp.add_condiments('蜂蜜芥末')  # 蜂蜜芥末为给add_condiments中condiments变量定义值
# 地瓜数据
print(sp) # 访问地瓜数据
