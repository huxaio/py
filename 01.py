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
# brith = int(t) # 类型转换，str => int

sum = 0
for x in [1,2,3,4,5,6,7,8]:   # for in 循环 另有 while 循环
    sum = sum + x
print(sum)
print(list(range(6))) # 生成整数序列