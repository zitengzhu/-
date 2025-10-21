from cnocr import CnOcr
#ocr方法返回的结果是列表，每个元素是包含text和position的字典，而非直接返回字典
'''
def img_1():
    img_name='b.png'
    a=CnOcr(det_model_name='naive_det')
    res=a.ocr('b.png')
    print(res)
    print(type(res))#数据类型为dict(字典)  字典由键值对构成 要想调用值 要打印键
img_1()

直接打印res会显示:
[{'text': '然后迅速退出你的账号', 'score': 0.21512137353420258, 'position': array([[         21,          43],
       [        268,          43],
       [        268,          58],
       [         21,          58]], dtype=float32)}]      



def img_1():
    img_name='b.png'
    a=CnOcr(det_model_name='naive_det')
    res=a.ocr('b.png')
    for i in res:
        print(i)
img_1()
将字典res中的所有值依次打印
将i循环赋值为res打印会显示:
[{'text': '然后迅速退出你的账号']
'''




def img_1():
    img_name='b.png'
    a=CnOcr(det_model_name='naive_det')
    res=a.ocr('b.png')
    for i in res:
        print(i['text'])
img_1()
#通过将i循环赋值为res并通过键(text)调用字典i中的值
#随后打印i会显示：
#然后现在迅速退出你的账号



