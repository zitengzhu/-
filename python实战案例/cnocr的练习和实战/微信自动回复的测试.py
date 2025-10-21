import pyautogui as pg
from cnocr import CnOcr
import time
import pyperclip
#loc_friend=pg.locateOnScreen('masge.png',confidence=0.9)
#print(loc_friend)
import random
'''
def get_mgs(new_loc):
    print('----------你有未读信息----------')
    time.sleep(1)
# 识别到未读信息进行点击 未读图标
    pg.click('img.png', clicks=1)
# 将鼠标自点击位置向做移动200个坐标
    loc_2 = (new_loc.left + 200)
# 鼠标移动单击打开好友秒天界面
    pg.click(loc_2, clicks=1)

# 通过masge.png定位微信快捷键位置
    loc_friend = pg.locateOnScreen('masge.png', confidence=0.9)
    print(loc_friend)
# 通过给出的loc_friend的坐标进行用户聊天记录的截图
    loc_3 = (int(loc_friend.left), int(loc_friend.top - 111), 915, 79)
    pg.screenshot('img_1.png', region=loc_3)
    
# 截图完成后用cnocr进行信息识别文字
    obj = CnOcr()
    res = obj.ocr('img_1.png')
    for i in res:
        xinxi = (i['text'])
        print(xinxi)
        return xinxi
        
         huifu='您好，由于工作繁忙暂时没有办法回复你的消息'
    pyperclip.copy(huifu)
    time.sleep(1)
    pg.hotkey('ctrl','v')您好，由于工作繁忙暂时没有办法回复你的消息
    
    time.sleep(1)
    pg.press('enter')

huifu='您好，由于工作繁忙暂时没有办法回复你的消息'
pyperclip.copy(huifu)
time.sleep(1)
pg.hotkey('ctrl', 'v')
time.sleep(1)
pg.press('enter')
'''
suiji=('你好','我很好','我也很好')
guding={'你好':'我还好',
        'hello':'ok',}
number=random.randint(0,len(suiji)-1)
a=input('请输入你想要的内容')
if a in guding :
    msg=guding[a]
    print(msg)
else:
    msg=suiji[number]
    print(msg)








