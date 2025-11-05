'''
该文件用于完成学生管理系统的具体业务操作，即：学生信息的增删改查，保存....
'''

# 导包
from student import Student
import time


# 创建学生管理系统类
class StudentCMS:
    def __init__(self):# [学生对象，学生对象，学生对象] ->[student(...),student(...),student(...)]
        self.stu_info = []
    @staticmethod
    def show_view():
        # 定义登录界面
        print('*' * 23)
        print('学生管理系统V2.0版')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询单个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t7.加载学生信息')
        print('\t0.推出系统')
        print('*' * 23)
    # 定义函数，添加学生信息
    def add_student(self):
        # 录入学生信息
        name = input('请录入学生姓名:')
        gender = input('请录入学生性别:')
        age = input('请录入学生年纪:')
        phone = input('请录入学生电话号码:')
        describe = input('请录入学生评价:')
        # 添加学生信息到列表
        stu = Student(name,gender,age,phone,describe)
        self.stu_info.append(stu)
        print(f'{name}信息录入完毕')
    # 定义函数，删除学生信息
    def del_student(self):
        del_student = input('请输入想要删除信息的学生姓名:')
        for data in self.stu_info:
            if data.name == del_student:
                self.stu_info.remove(data)
                print(f'学生{del_student}的信息删除成功\n')
                break
        else:
            print('查无此人')
    # 定义函数，修改学生信息
    def update_student(self):
        upd_student = input('请输入想要修改信息的学生姓名:')
        for data1 in self.stu_info:
            if data1.name == upd_student:
                data1.age=int(input('请录入新的年龄数据：'))
                data1.gender=input('请录入新的性别数据：')
                data1.phone=input('请输入新的电话信息：')
                data1.describe=input('请输入新的学生评价')
                print(f'学生{data1.name}的信息修改成功')
                break
        else:
            print('查无此人')
    # 定义函数，查询单个学生信息
    def search_one_student(self):
        search_student = input('请输入想要查找信息的学生姓名:')
        for data2 in self.stu_info:
            if data2.name == search_student:
                print(data2)
                break
        else:
            print('查无此人,请重新输入\n')
    # 定义函数，查询所有学生信息
    def search_all_student(self):
        if len(self.stu_info)==0:
            print('暂无数据')
        else:
            for stu in self.stu_info:
                print(stu)
            print()
    # 定义函数，保存学生信息
    def save_student(self):
        with open('data.txt','w',encoding='utf-8') as f:
            stu_dict = [stu.__dict__ for stu in self.stu_info]
            f.write(str(stu_dict))
    # 定义函数,加载学生信息
    def load_student(self):
        try:
            with open('data.txt','r',encoding='utf-8') as f:
                stu_data= f.read()
                stu_list = eval(stu_data)
                if len(stu_list)==0:
                    stu_list=[]
                self.stu_info = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            with open('data.txt','w',encoding='utf-8') as f:
                pass
    # 定义函数，将所有功能串联
    def star(self):
        # 加载学生信息
        self.load_student()
        # 设置死循环达到重复执行的目的
        while True:
            # 加入休眠让效果更好
            time.sleep(1)
            StudentCMS.show_view()
            user = input('请输入您想要执行的操作')
            if user == '1':
                print('正在执行[添加学生信息]操作')
                self.add_student()
            elif user == '2':
                print('正在执行[删除学生信息]操作')
                self.del_student()
            elif user == '3':
                print('正在执行[修改学生信息]操作')
                self.update_student()
            elif user == '4':
                print('正在执行[查询单个学生信息]操作')
                self.search_one_student()
            elif user == '5':
                print('正在执行[查询所有学生信息]操作')
                self.search_all_student()
            elif user == '6':
                self.save_student()
                print('学生信息保存成功')
            elif user == '7':
                print('学生信息加载完毕')
                self.load_student()
            elif user == '0':
                obj = input('您确定要推出系统吗？（Y/N）->')
                if obj.lower() == 'y':
                    self.save_student()
                    print('退出系统，欢迎下次使用')
                    break
                else:
                    print('录入错误，请重新录入')


if __name__ == '__main__':
    s = StudentCMS()
    s.star()
