# 使用def定义一个函数
def say_hello(arg):
    print("hello " + arg)
    return "hello " + arg
# 调用函数
say_hello("world")
# 函数的返回值
result = say_hello("world")
print(result)
# 当我们的参数为两个列表且在做加法运算时 python会自动将两个列表进行合并

def merge_list(list1, list2):
 return list1 + list2
list1 = [1, 2, 3,4]
list2 = [4, 5, 6]
print(merge_list(list1, list2))

#使用kv对方式传值 在我们使用kv对的时候如果要和普通参数混合使用则需要将普通参数提钱
def say_hello(name, age):
    print("hello " + name + " you are " + str(age) + " years old")
say_hello(name="world", age=18)
def test_int(name,age):
    print("hello " + name + " you are " + str(age) + " years old")
test_int('beloved',age=18)
#使用默认参数和任意参数
def test_default(name, age=18):
    print("hello " + name + " you are " + str(age) + " years old")
test_default("world")
#在某些时候我们并不知道我们需要传入多少个实参此时我们可以将形参定义为任意参数
def test_ari(name, *args):
    print("hello " + name)
    print(args)
test_ari("world", 18, "male", "student")
#在python中我们也可以使用kv对的方式传入参数
def key_test(key2,key1,key3):
    print(key1,key2,key3)
key_test(key2="diy",key1="hello",key3="beloved")
# 可变类型传参 使用*args可以允许我们传入多个不同类型的参数 但是不能通过kv对进行传值
def test_anytype(*args):
    print(type(args))
test_anytype("world",'出生')
# 可变关键字传递参数
def test_key(**kwargs):
    print(kwargs)
test_key(host="127.0.0.1", port=3306,username='beloved')
# 混合传递参数顺序 优先使用位置参数 然后是任意参数 最后是任意kv对参数
def test_mix(name, age, *args, **kwargs):
    print(name, age, args, kwargs)
test_mix("world", 18, "male", "student", host="127.0.0.1", port=3306, username="beloved")
# 使用key_world only参数 规定必须传入对应k的值
def test_keyworld_only(*, name, age):
 print(name, age)
test_keyworld_only(name="world", age=18)
def testkeyworld_t(*args,x,y,**kwargs):
    print(args,x,y,kwargs)
testkeyworld_t(x=1,y=2)
def testK (*,k,v):
    print(k,v)
testK(k=1,v=2)
# 使用positional_only参数规定必须传入位置参数
def test_positional_only(a,b ,/,c):
    print(a,b,c)
test_positional_only(1,2,3)