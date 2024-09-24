def foo(a):
    def bar(y):
        def ker(x):
            return  a+y+x
        return  ker
    return bar
print(foo(4)(5)(6))
def foo1(a):
    def bar(x,y):
        return  a+x+y
    return bar
print(foo1(4)(5,6))
#柯里化的主要目的是为了保持函数事务处理的单一性一个函数部分处理一个事物,本质上也是利用了闭包的原理


