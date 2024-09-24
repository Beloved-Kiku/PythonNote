#高阶函数的定义
#在python中高阶函数的定义:当一个函数接受的形参含有函数或者一个函数的返回值是一个函数时,这样的函数被称作为高阶函数
def foo(num:int=1):
    def bar ():
        nonlocal  num
        num +=1
        return num
    return bar
#创建变量接受引用值
f1 = foo(1)
f2 =foo(2)
#函数每次调用都将在Stack中创建一个临时栈帧,每一个栈帧都是一个独立的引用值 所以当我们调用函数时所创建的栈帧都是全新的栈帧
#在python中正因为每一个函数都会独立创建栈帧所以我们不能通过任何方法对函数进行判断是否相等 都会返回false
print(f1())
print(f2())
print(f1 ==f2)
print(f1 is  f2)
def counter(base):
    def inc(step=1):
        nonlocal base
        base+=step
        return  base
    return  inc
#自定义sorted函数
#使用冒泡排序筛选最大值
def FindMax(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def FindMin(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return  arr
#reverse默认接受两个参数第一个为升序或者降序 第二个为key
def Reverse(a=None,b=None):
    if a =='up':
        return  FindMax
    if a =='down':
        return FindMin
def Sorted(list):
   return  FindMax(list)
print(Sorted([3,2,1]))