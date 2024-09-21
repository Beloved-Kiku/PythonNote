#在python中的作用域分为全局作用域和函数局部作用域
#全局作用域：在函数外部定义的变量，作用域为全局作用域，全局作用域的变量在函数内部可以访问
#局部作用域：在函数内部定义的变量，作用域为局部作用域，局部作用域的变量在函数外部无法访问
#在python中没有变量提升的说法 ，变量在函数内部使用之前必须先定义 如果我们在一个函数内出现了变量赋值那么python解释器就会把它看作是局部变量
num = 10
y =20
def Area_test(x:int=1):
    print(num,'局部访问全局成功')
  #  y =y+1 #这里我们对x进行了赋值，所以x变成了局部变量,此时我们内部并没有定义x所以python会报错
    print(y)
    return  'Success'
print(Area_test())
def k():
    def g():
        return  '1'
    return g()
c =k()
print(c)
#函数闭包问题
def foo():
    x = 1
    print(x)
    def bar():
        nonlocal x
        x +=1
        return x
    return bar
f = foo()
#在上面代码中我们将foo()调用后的值给了f变量,f变量其实是一个函数bar()的引用
#所以当我们在执行f()时 其实是在执行bar() 但是此时foo()函数已经执行完毕了,x位于foo函数里的变量应该被回收
#但是因为bar函数中的x指向了foo函数中的x的值,所以此时应该是foo函数中x与x所对应的值断开联系,且foo函数中的x标识符被回收(仅仅x 不是x所对应的值)
#但是此时bar函数中的x指向了foo函数中x指向的值,所以python将 bar函数中的x+=1,中的x指向了,foo函数中x指向的那个地址值
#所以当我们每调一次f()时x+=1其实就去寻找x指向的那个值
#简而言之就是我们可以理解为这个函数外层函数已经销毁了,它函数体内的变量标识符也销毁了,但是因为内部函数引用了这个变量所对应的值,所以在python内部将这个值的地址值和内部引用的变量建立一个联系
print(f())
print(f())
print(f())

#函数形参作用域问题(引用类型)
def foo1(x=[]):
    x.append(1)
    return x
print(foo1.__defaults__)
print(foo1())
print(foo1())
print(foo1())
#当我们在为函数形参设置一个引用类型的参数时 python会讲这个值放在对应函数的__defaults__中,当我们调用函数时,python会先去__defaults__中寻找这个参数的值,如果找到了就使用这个值,如果没找到就使用默认值
#所以当我们多次调用函数时,这个参数的值会一直累加,因为每次调用函数时,python都会去__defaults__中寻找这个参数的值,如果找到了就使用这个值,如果没找到就使用默认值
# 关于+=和 +的区别
#当我们对引用可变类型使用+=的时候我们会对这个引用类型数据进行就地修改
def test_copy(x=[]):
    x+=[1] #等效于x.extend([1])就地修改源地址上的值
    print(x)
    return x
print(test_copy(),'change1')
print(test_copy(),'change2')
print(test_copy(),'change3')
#当我们对引用类型使用+的时候我们会对这个引用类型数据进行复制一份,然后对复制的数据进行修改
def test_copy1(x:int):
    x=x+1
    print(x)
    return x
print(test_copy1(1),'copy1')
print(test_copy1(1),'copy1')
print(test_copy1(1),'copy1')
#当我们对引用不可变类型使用+=的时候我们会对这个引用类型数据进行复制一份,然后对复制的数据进行修改
test = tuple([1,2])
print(id(test),'未修改前的地址')
test +=(3,)
print(id(test),'修改后的地址',test)
#因为元组为不可变类型所以一旦创建其对应的地址值就不能被修改所以+=在这里其实就等于 test = test+(3,)
#会创建一个新的元组保留我们这次修改的数据
x =1
print(id(x),'未修改前的地址')
x+=1
print(id(x),'修改后的地址',x)