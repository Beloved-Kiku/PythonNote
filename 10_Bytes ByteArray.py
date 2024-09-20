#bytes一旦经过定义后就不可被修改类似于常量字符串,而bytesArray则可以修改 类似于list
#bytes 可以通过偏移量进行访问
# 定义一个bytes的方法
a = bytes()
b = b'hello world' # b表示bytes类型
print(b)
#bytes 中接受一个可迭代的int类型参数  1byte = 8bit  最多可容纳表示的范围是0-255
#使用bytes 生成大小写的26字母
c= bytes(range(97, 123))
d = bytes(range(65,91))
print(c)
print(d)

#bytesArray 本质上也是一个list 它可以使用列表提供的各种api
arr = bytearray()
# 当我们要修改bytearray时 我们输入的每一个int值要确保在0-255之间
arr.append(65)
print(arr)
# bytearray 可以通过索引进行修改
arr[0] = 97
print(arr)
# bytearray 可以通过切片进行修改
arr[0:3] = bytes(range(97,100))
print(arr)
# bytearray 可以通过切片进行删除
del arr[0:3]
print(arr)
# bytearray 可以通过切片进行插入
arr[0:0] = bytes(range(97,100))
print(arr)
# bytearray 可以通过切片进行替换
arr[0:3] = bytes(range(65,68))
print(arr)
# bytearray 可以通过切片进行复制
arr[0:3] = arr[0:3]
