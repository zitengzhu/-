class Car:
    def __init__(self,color,number):
        self.color = color
        self.number = number
    def show(self):
        print(f'颜色:{self.color},轮胎数量:{self.number}')
'''

这种写法是对的
c1 =Car('红色',6)


这种写法是错的
c1 = Car()
c1.number=4
c1.color='红色'
'''