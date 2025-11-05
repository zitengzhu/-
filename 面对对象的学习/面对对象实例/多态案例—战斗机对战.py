'''
案例：构建对象对战平台
    1.英雄一代机(战斗力60)与敌军战机(战斗力70)对抗。英雄一代机失败
    2.卧薪尝胆，英雄二代机(战斗力80)出场！战胜敌军战机
    3.在队长平台进行对战，在代码不发生改变的情况下，完成多次战斗

代码提示：
    英雄一代机 HeroFighter
    英雄二代机 Pro HeroFighter
    敌军战机 EnemyFighter
'''

class HeroFighter:
    def power(self):
       return 60

class ProHeroFighter(HeroFighter):
    def power(self):
        return 80

class EnemyFighter:
    def power(self):
        return 70

def fighter(h:HeroFighter,e:EnemyFighter):
    # 限制 h参数只能是HeroFighter类以及其子类的数据 e参数只能是EnemyFighter类以及其子类的数据
    if h.power()>e.power():
        print('英雄级获得胜利')
    else:
        print('敌军战机获得胜利')


# 英雄一代机V敌军战机
h1 = HeroFighter()
e1 = EnemyFighter()
fighter(h1,e1)

# 英雄二代机V敌军战机
h2 = ProHeroFighter()
e1 = EnemyFighter()
fighter(h2,e1)
