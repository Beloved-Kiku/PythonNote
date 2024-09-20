# 常见运算符 + - * /(商一定是浮点数)
# //(取整除) 不管结果怎么样向下取整若结果有浮点数则用浮点数表示
# %取模(取余数)
# **取次方
# 优先级排序 幂>x>/>%>//>+-
from IPython.utils.coloransi import value

a =4
b=2.2
print(a//b)
print(a%b)
#转义字符\t 占四个字符 \n换行字符 \r表示将当前位置移动到开头 \\ ==\
pwd = input('请输入密码:')
print(pwd)
# 定义年龄变量
age = 19
# 如果年龄小于18
if age<18:
    # 打印NO
    print('NO')
# 如果年龄大于18
elif age>18:
    # 打印Yes
     print('Yes')
# == 判断两个变量是否相等  !=判断两个变量是否不等 可以配合type使用进行类型判断
# 逻辑运算符 与或非  与(and) 或(or) 非(no)
else:
    print('No')

day = input('今天是周几:')
station = 'car'
if day=='5':
    if station=='car':
        print('yes')
    else:
        print('no')
else:
    print('今天不是周末')

str = '12345'
for i  in str:
    print(i)
value = 0
for i in range(1,101,1):
 value += i
print(value)