#装饰器通常是用来装饰函数或者类
#在实际开发中非业务代码写在业务代码中我们一般不推荐这么做
#装饰器的作用就是将多个业务的通用型功能代码抽离形成一个独立的函数通过功能型函数完成
#使用柯里化完成一个函数计算函数装饰器
import  datetime
import time
def ComputedFun(fn):
    def wrapper(*args,**kwargs):
        print('函数调用前todoSomething')
        start = datetime.datetime.now()
        Etv=   fn(*args,**kwargs)
        # 利用闭包fn记住我们传入的add函数 并且将 add函数地址值返回给Etv
        #wrapper返回add函数的地址值 被新的变量标识符保存
        print(f"Function took {(datetime.datetime.now()-start).total_seconds()}s")
        return Etv
    return  wrapper
#使用@xxx语法糖会将后面的第一个函数标识符作为参数传递给我们的装饰器 等价为 add = ComputedFun(add) 这就叫无参或者单参装饰器
# wrapper = copy_properties(wrapper)
@ComputedFun
def add(x,y):
    time.sleep(2)
    return x+y
add(10,20)