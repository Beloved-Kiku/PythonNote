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