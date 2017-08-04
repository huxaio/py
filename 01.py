# -*- coding: utf-8 -*-
classmate = ["mc","bob","tr"]  # list类型
print(len(classmate))
print(classmate[-1])
classmate.append("am") # 追加
classmate.insert(1,"jk") # 插入
classmate.pop()  # 删除末尾元素
classmate.pop(1) # 删除指定位置
classmate[1] = "sh" # 赋值指定位置
print(classmate)

t = (1,) # tuple类型 只读 
# brith = int(t) # 类型转换，str => int(整数)，float(浮点)，str(字符串),bool(布尔值)

sum = 0
for x in [1,2,3,4,5,6,7,8]:   # for in 循环 另有 while 循环
    sum = sum + x
print(sum)
print(list(range(6))) # 生成整数序列

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-3))
# L[::5] 所有数，每5个取一个。
listfor = [x*x for x in range(1,11) if x % 2 == 0]
print(listfor)