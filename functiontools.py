from functools import reduce
#reduce函数接收两个参数可以将上一个函数的返回值作为下一次计算的x值
def fn(x,y):
    return  x+y
def CountValue():
     return  reduce(fn,range(1,11) ,100)
print(CountValue())
#lru进行函数缓存 若函数输入一样则会使用缓存的结果作为返回而函数体不会再执行
from  functools import  lru_cache
@lru_cache()
def add (x=4,y=5):
    print('-'*30)
    return  x+y
print(add(5,6))
print(add(5,6))
print(add(x=5,y=6))