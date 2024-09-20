# 单行注释
# 首次创建变量时会在内存中开辟新的空间 后续修改只会修改地址值
# 变量严格区分大小写 不能以数字下划线开头不能使python中已经使用的关键字
num = 1
print(num)
# 整形 Int  Float 浮点型 Boolean型(可当作整型对待) String型 Complex型 包含实部虚部  固定写法:z =a+bj --a为实部 b为虚部 j为虚部单位
print(type(123),type('javaScript'),type(True),type(True+False))
print((1+2j)+(2+3j))
#占位符 % format %s(字符串) %d(整形)
name= 'LYC'
age =20
print('我的名字是:%s 我的年龄是%d', name,age)
# 可以设置数字位数 %5d 设置整形为5位 若在最前面则使用空白补
# %05d 表示五位数 若不足五位则使用0补全
print('%5d'%age)
# %f 浮点数 默认6位置 不足则在后面补0 若超出6位则按照四舍五入进行舍去
print('%f' %1.23)
# %.3f 设置三位小数
print('%.3f' %1.23456)

