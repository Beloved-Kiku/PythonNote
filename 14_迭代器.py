#在python中由迭代器所创建的对象我们称为惰性对象
#惰性对象：在需要的时候才去计算值，而不是在创建对象的时候计算值
#惰性对象的好处：节省内存，提高效率
#惰性对象的使用：通过生成器函数创建惰性对象，通过生成器表达式创建惰性对象
#定义一个惰性对象
lazy_obj =(x for x in range(10))
print(next(lazy_obj))
print(next(lazy_obj))
#惰性对象的使用 惰性对象只会被遍历一次
for x in lazy_obj:
    print(x)
#我们也可以使用next函数来获取惰性对象的值 前提是惰性对象没有被提前next 或者循环过
