#在python中函数在调用的时候会被添加到栈stack中形成一个栈帧,当该函数执行完毕之后会被栈弹出,而栈作为一种后进先出的数据结构所以
#而我们的变量的值 list 元组 字典的数据会被堆(heap)记录 我们所进行的变量赋值其实讲堆中的数据引用地址给变量标识符
def foo1(b,b1=3):
    print("fool called" ,b ,b1)
def foo2(c):
    foo3(c)
    print("foo2 called",c)
def foo3(d):
    print("foo3 called",d)
def main():
    print("main called")
    foo1(100,101)
    foo2(200)
    print("main ending")
main()
#在上面的代码中依次执行的函数是Main->foo1->foo3->foo2
#首先当我们调用main函数的时候在我们的Stack将会把Main作为栈帧添加到栈的最底部在Main栈帧中会输出print->调用foo1函数
#此时Main函数调用了foo1函数那么foo1函数会被作为栈帧添加到栈中,因为我们传递了100和101参数所以在foo1栈帧中会最先执行 b=100 b1=101 然后执行print
#当foo1函数执行完毕后 此时我们并不会先去讲foo2函数添加到栈中,而是讲foo1整个栈帧从栈中弹出,在弹出的时候python会去查看由 b 和 b1 引用的数据 有没有被别的变量或者函数引用
#如果有的话则将b和b1标识符切断引用,但是不会将引用的数据清除,然后将整个foo1从栈中弹出
#当foo1弹出后foo2被调用放在栈中,此时foo2 首先进行c=200的赋值操作,然后接着调用foo3将foo3加入栈中 在foo3函数中首先进行 d=c 然后输出print语句
#随后foo3执行完毕,在foo3函数被弹出栈之前python发现 d=c=200 而c又在foo2函数中 所以此时200在堆中的引用计数是2,所以python将foo3函数中的d标识符与200的引用断开,然后将foo3弹出
#foo3弹出后此时foo2的处于栈顶继续执行foo2中的打印语句然后将foo2弹出
#当Main函数中的所有函数都被调用完毕弹出后此时Main函数位于栈顶将继续执行print语句,随后被弹出栈,至此一个函数的调用->执行->销毁 已经完成
