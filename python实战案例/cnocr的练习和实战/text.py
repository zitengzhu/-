import random
import time
str=('qwertyuiopasdfghjklzxcvbnm')
new_list=random.sample(str,3)
print(new_list) #list
new_str=''.join(new_list)
print(type(new_str)) #<class 'str'>