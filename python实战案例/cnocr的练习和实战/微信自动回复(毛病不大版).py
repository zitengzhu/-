'''
1 打开微信
2进行判断是否有新消息
 2.1 有新消息就进入发消息的人的微信聊天页面
 2.2 没有消息就在微信聊天界面待机
3进入发消息的人的聊天界面内就识别发送的消息内容并回复
'''
import pyperclip
import time
import pyautogui as pg
from cnocr import CnOcr
import random
# 1根据在文件区截取的微信图片识别微信在桌面的位置
loc=pg.locateOnScreen('vx.png',confidence=0.9)
print(loc)
# 1.1获取到微信的坐标后进行双击打开
pg.click(loc,clicks=2)
time.sleep(0.5)
def run():
# 2打开微信之后进行循环消息识别如果有未读消息就进入与未读消息用户的聊天框
    while True:
        time.sleep(1)
        try:
            #识别是否有未读消息
            new_loc=pg.locateOnScreen('img.png',confidence=0.7)
            # 确认img.png的坐标
            print(new_loc)
            # 接受信息
            xinxi=get_mgs(new_loc)
            #回复信息
            send_msg(xinxi)
        except:
            time.sleep(1)
            print('----------目前没有新消息----------------')

def get_mgs(new_loc):
    print('----------你有未读信息----------')
    time.sleep(2)
# 识别到未读信息进行点击 未读图标
    pg.click('img.png', clicks=1)
# 将鼠标自点击位置向右移动200个坐标
    loc_2 = (new_loc.left + 200)
# 鼠标移动单击打开好友秒天界面
    time.sleep(2)
    pg.click(loc_2, clicks=1)
    time.sleep(2)
# 通过masge.png定位微信快捷键位置
    loc_friend = pg.locateOnScreen('masge.png', confidence=0.9)
    #print(loc_friend)
# 通过给出的loc_friend的坐标进行用户聊天记录的截图
    loc_3 = (int(loc_friend.left), int(loc_friend.top - 111), 915, 79)
    pg.screenshot('img_1.png', region=loc_3)
# 截图完成后用cnocr进行信息识别文字
    obj = CnOcr(det_model_name='naive_det')
    res = obj.ocr('img_1.png')
    for i in res:
        xinxi=i['text']
        print(xinxi)
        return xinxi
def send_msg(xinxi):
    suiji = ('你好', '我很好', '我也很好')
    guding = {'你好': '我还好',
              '我': 'ok', }
    number = random.randint(0, len(suiji) - 1)
    if xinxi in guding :
        msg = guding[xinxi]
    else:
        msg = suiji[number]
    pyperclip.copy(msg)
    time.sleep(1)
    pg.hotkey('ctrl', 'v')
    time.sleep(1)
    pg.press('enter')
run()