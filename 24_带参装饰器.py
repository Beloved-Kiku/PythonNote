#使用柯里化定一个修改__name__和__doc__的装饰器
from curses import wrapper


def ChangePrototype(add):
    def _copy(wrapper):
        wrapper.__name__ = add.__name__
        wrapper.__doc__ = add.__doc__
        #需要将修改后的wrapper返回出去作为因为这个函数的返回值决定了 第一个无参装饰器的返回值 若不return 则是none
        return wrapper
    return _copy
#定义一个无参装饰器接受一个函数
def ComputedFun(fn):
    #这里的fn是我们最开始传入的add函数 所以我们要修改add的__name__ 和__doc__应该从这里入手
    #这里的装饰器应该接收fn 和 wrapper函数 然后进行修改
    #使用语法糖这句话本质是= wrapper = ChangePrototype(fn)(wrapper)
    #此时wrapper指向的就是ChangePrototype函数的返回值
    @ChangePrototype(fn)
    def wrapper(*args, **kwargs):
     """
     this is wrapper function Return
     """
     print('add函数调用前增强')
     result = fn(*args,**kwargs)
     print('add函数调用后的增强')
     return result
    return wrapper
#使用无参装饰器进行执行函数
# 此时 add =Computed(add) 本质上add保存的是wrapper函数的地址值
@ComputedFun
def add(x,y):
    """
    this is Add Function
    :param x:
    :param y:
    :return: x+y
    """
    return x+y
print(add(1,2))
print(add.__name__,add.__doc__) #print wrapper
#使用参数装饰器修改add的__name__ 和__doc__