#LEGB规则：L：local，E：enclosing，G：global，B：built-in
#L：局部作用域，E：外部嵌套函数作用域，G：全局作用域，B：内建作用域
#优先级：L > E > G > B
#Local指函数自身的局部变量,函数调用时创建,若无闭包则函数调用结束后销毁
#Enclosing指嵌套函数的外部函数的局部变量,函数调用时创建,若无闭包则函数调用结束后销毁
#Global指全局变量,函数调用时创建,程序结束销毁
#Built-in指内建变量,从python解释器启动开始创建,程序结束销毁(print open 等内置函数)
#在python中对象的销毁其实就是引用计数清零然后通过gc进行回收
#使用del的本质上是将对象命名在命名空间中删除 然后将他所对应的地址值引用计数-1
#如果引用计数为0则说明没有变量引用该对象 则该对象会被gc回收
#使用同名标识符号则后出现的标识符会覆盖前面的标识符但是引用计数不会改变
#当python结束运行时候所有对象销毁
import sys
def foo():
    return 'beloved'
a =foo
b =foo
del foo
# foo名字在命名空间中被删除但是foo所指向的地址值仍然被ab引用
print(sys.getrefcount(a)) #4
c =a
d =a
print(sys.getrefcount(a))
print(sys.getrefcount(a)) #4
print(a,b,c,d)

