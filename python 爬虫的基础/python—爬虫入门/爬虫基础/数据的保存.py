# with open() as XXX  用来保存数据


# 如果要保存的数据是图片 音频 视频 就是两个参数
# 第一个参数是图片的名称  第二个参数是想要保存的方式
# 图片 音频 视频属于二进制文件所以保存时在第二个参数后要加b
# wb 写入数据  rb 读取数据
# with open('想要保存的二进制数据的名称','wb') as f:
    # f.write() 括号内存放想要保存的数据  二进制数据的保存时要加.content的后缀
# 具体案例看python_爬虫文件中的图片的保存


# 保存除图片 音频 视频外的内容就是三和参数
# 第一个参数是图片的名称 第二个参数是想要保存的方式 r(read 读取) w(write 写入 会覆盖之前的数据) a(add 追加写入 不会覆盖)
# 第三个参数是编码格式encoding="utf-8"\
# 写入数据
with open('a.text','w',encoding='utf-8') as f:
    f.write('333')  # + \n可以实现换行

#读取数据
with open('a.text','r',encoding='utf-8') as f:
    # 数据需要变量来接受
    a=f.read()
    print(a)