#元组定义 元组内可以存放不同数据类型的数据 元组不可变
tuple1 = (1,2,3,4,5)    #tuple1 = 1,2,3,4,5
tuple2 = (1,"hello",True)    #tuple2 = 1,"hello",True
tuple3 = (1,2,3,4,5,6,7,8,9,10)    #tuple3 = 1,2,3,4,5,6,7,8,9,10
print(tuple3)
#元组取值方法和列表一样 ，通过索引取值 ，也可以切片 取值
print(tuple3[0])    #输出第一个元素
print(tuple3[0:3])    #输出前三个元素
print(tuple3[-1])    #输出最后一个元素
print(tuple3[-3:])    #输出最后三个元素
#通过 index count len 等方法操作元组
print(tuple3.index(5))    #输出元素5的索引
print(tuple3.count(5))    #输出元素5的个数
print(len(tuple3))    #输出元组的长度
#元组不能增删改元素，只能读取
#tuple3[0] = 100    #报错
#tuple3.append(100)    #报错
#tuple3.remove(5)    #报错

#字典
dict1 = {"name":"张三","age":18,"gender":"男"}    #dict1 = {"name":"张三","age":18,"gender":"男"}
print(dict1)    #输出字典
#根据key获取字典中的值
print(dict1["name"])    #输出字典中key为name的值
#根据key修改字典中的值
dict1["age"] = 20    #修改字典中key为age的值为20
print(dict1)    #输出字典
#根据key删除字典中的值
del dict1["gender"]    #删除字典中key为gender的值
print(dict1)    #输出字典
#字典的遍历
for key in dict1:
    print(key,dict1[key])    #输出字典中的key和value
for key,value in dict1.items():
    print(key,value)    #输出字典中的key和value
#字典的常用方法
print(dict1.keys())    #输出字典中的key
print(dict1.values())    #输出字典中的value
print(dict1.items())    #输出字典中的key和value
#使用for循环取出key
for key in dict1.keys():
    print(key)    #输出字典中的key
#使用for循环取出value
for value in dict1.values():
    print(value)    #输出字典中的value
#使用for循环取出key和value
for key,value in dict1.items():
    print(key,value)    #输出字典中的key和value
print(dict1.get("name"))    #输出字典中key为name的值
print(dict1.get("name1"))    #输出字典中key为name1的值，如果不存在则返回None
print(dict1.get("name1","不存在"))    #输出字典中key为name1的值，如果不存在则返回"不存在"
print(dict1.pop("age"))    #输出字典中key为age的值，并删除该key和value
print(dict1)    #输出字典
print(dict1.popitem())    #输出字典中最后一个key和value，并删除该key和value
print(dict1)    #输出字典
print(dict1.clear())    #清空字典
print(dict1)    #输出字典



