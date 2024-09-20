#使用列表解析式在大多数情况下可以提高执行效率
#通常列表解析式用来初始化一个列表或者对列表中的数据做一些判断填充 返回一个新的列表
newlist = [i for i in range(10)]
print(newlist)
#列表解析式可以嵌套
newlist = [i for i in range(10) for j in range(10)]
print(newlist)
#列表解析式可以添加条件配合if语句进行使用
newlist = [i for i in range(10) if i % 2 == 0]
print(newlist)
#列表解析式+多个条件使用
newlist = [i for i in range(10) if i % 2 == 0 if i % 3 == 0]
print(newlist)
newlist = [i for i in range(20) if i % 2 == 0 or i % 3 == 0]
print(newlist)