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

#定义一个生成器对象
#如果我们不将生成器函数的地址值给赋值的话那么每调用一次next生成器会生成一个全新的生成器对象
#每当我们使用next函数的时候，生成器函数会从上一次yield语句的下一行开始执行，直到遇到下一个yield语句或者return语句
def lazy_obj2():
    for b1 in range(10):
        yield '第一次'
        print('2')
        yield '第二次'
        return '报错'
n = lazy_obj2()
print(next(n))
print(next(n))
#当生成器遇到return语句时，生成器会抛出StopIteration异常，表示生成器已经没有值了且我们获取不到return的值
#生成器非常适合处理数据流、无限序列、或大数据集，具有延迟计算特性。
#迭代器更适合需要精细控制迭代过程的场景，比如在自定义数据结构上进行迭代
#生成器通常更高效，因为它们是“惰性”的，只在需要时才生成值。
#迭代器的实现可能会在某些场景下占用更多内存，特别是当它们预先生成所有数据时。
def foo ():
    i = 0
    def bar():
        nonlocal  i
        i =i+1
        return i
    return bar
c = foo()
print(c())
print(c())
print(c())
#使用闭包加生成器完成调用计数+1 核心:保留生成器上一次的值 使得我们最终只创建一个生成器 而不是多次调用创建全新的生成器


