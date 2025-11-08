'''
案例：演示python内置的__dict__属性

__dict__属性介绍：
    它是python内置的属性，可以把对象转成字典形式
'''
#
# from student import Student
# s1=Student('aaa','aaa','a','a','a')
# print(s1)  # 姓名:aaa,性别:aaa,年龄:a,手机号:a,评语:a
#
# s1_dict=s1.__dict__
# print(s1_dict)  # {'name': 'aaa', 'gender': 'aaa', 'age': 'a', 'phone': 'a', 'describe': 'a'}
#
# # 学生对象转化为列表
# s2=Student('bbb','bbb','b','b','b')
# s3=Student('ccc','ccc','c','c','c')
# stu_list=[s1,s2,s3]
#
# # 列表推导式
# list_dict = [stu.__dict__  for stu in stu_list ]
# print(list_dict)  # [{'name': 'aaa', 'gender': 'aaa', 'age': 'a', 'phone': 'a', 'describe': 'a'}, {'name': 'bbb', 'gender': 'bbb', 'age': 'b', 'phone': 'b', 'describe': 'b'}, {'name': 'ccc', 'gender': 'ccc', 'age': 'c', 'phone': 'c', 'describe': 'c'}]
#
# # {'name': 'aaa', 'gender': 'aaa', 'age': 'a', 'phone': 'a', 'describe': 'a'}转化为学生对象
# my_dict={'name': 'aaa', 'gender': 'aaa', 'age': 'a', 'phone': 'a', 'describe': 'a'}
# s4=Student(**my_dict)
# print(s4)  # 姓名:aaa,性别:aaa,年龄:a,手机号:a,评语:a
