# in 判断字符串中是否含有指定元素  若符合要求则返回True 否则返回False
print("hello" in "hello world")  # True
print("hello" in "hello world")  # False
print("hello" not in "hello world")  # False
print("hello" not in "hello world")  # True
# 判断字符串是否以指定元素开头(可检测多个字符串)可指定起止位置
print("hello world".startswith("hello"))  # True
print("hello world".startswith("world"))  # False
print("hello world".startswith(("hello", "world")))  # True
print("hello world".startswith(("python", "world")))  # False
print("hello world".startswith("hello", 0, 5))  # True
print("hello world".startswith("world", 0, 5))  # False
# 判断字符串是否以指定元素结尾(可检测多个字符串)可指定起止位置
print("hello world".endswith("world"))  # True
print("hello world".endswith("hello"))  # False
print("hello world".endswith(("hello", "world")))  # True
print("hello world".endswith(("python", "world")))  # False
print("hello world".endswith("world", 0, 5))  # False
print("hello world".endswith("hello", 0, 5))  # True
# 判断字符串是否为数字
print("123".isdigit())  # True
print("123a".isdigit())  # False
# 判断字符串是否为字母
print("abc".isalpha())  # True
print("abc123".isalpha())  # False
# 判断字符串是否为字母或数字
print("abc123".isalnum())  # True
print("abc123.".isalnum())  # False
# 判断字符串是否为空格
print(" ".isspace())  # True
print("a".isspace())  # False
# 字符串拼接
print("hello" + "world")  # helloworld
# 字符串重复输出
print("hello" * 3)  # hellohellohello
# 字符串切片
print("hello world"[0:5])  # hello
print("hello world"[6:11])  # world
# 字符串替换 可指定替换次数
print("hello world".replace("world", "python"))  # hello python
print("hello world".replace("world", "python", 1))  # hello python
# 字符串查找 若存在则返回对应下标 不存在则返回-1
print("hello world".find("world"))  # 6
print("hello world".find("python"))  # -1
# 字符串查找 index 若未找到则报错
print("hello world".index("world"))  # 6
# print("hello world".index("python"))  # 报错
# 统计字符串中指定元素出现的次数  可指定起止位置可省略开始和结束参数则默认寻找整个字符串
print("hello world".count("l"))  # 3
print("hello world".count("l", 0, 5))  # 2
# 字符串分割 可指定分割次数 可指定分割符  若不指定分割符则默认以空格分割
print("hello world".split(","))  # ['hello', 'world']
print("hello world".split("o", 1))  # ['hello', 'world']
print("hello world".split())  # ['hello', 'world']
# 字符串大小写转换
print("hello world".upper())  # HELLO WORLD
print("hello world".lower())  # hello world
# 字符串去除空格
print(" helloworld".strip())  # hello world
# 字符串长度
print(len("hello world"))  # 11
