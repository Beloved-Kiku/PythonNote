def fn (*nums):
    print(nums)
    results = 0
fn(1,2,3)
fn(*[1,2,3])
# 1. 函数参数解构
def fn2(**kwargs):
 print(kwargs)
fn2(name='张三',age=18)
fn2(**{'name':'张三','age':18})   # 使用**进行对字典结构会解构为 kv对的传递参数形式 name = '张三',age=18