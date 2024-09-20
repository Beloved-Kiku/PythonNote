from numpy import number

a=[[1]]
b = a*3
b[1][0] =100
print(b)

c =list(range(4))
d=list(range(4))
print(c==d)  # 在python中如果列表两个值完全一样会被判定为相等
print(id(c),id(d))
# 因为c和d都是list类型，list类型在内存中存储的是地址值，所以c和d的地址值是相同的，所以c==d为True 那么==比较的是引用数据的地址值而不是本身
e =c # 将c的地址值指向e 此时 e就是c c就是e
c[2] =10 #修改c的数据 e也会变 此时 c和e 都是 [1,2,10,3]
print(c)
print(c==d)
print(c==e)

ab =[1,[2,3,4],[5]]
cd = ab.copy()
print(ab==cd)

abc = [1,[2,3,4],[5]]
bcd = abc.copy() # 这个时候执行的是复制操作会在堆中开辟一个新的地址空间分配给bcd
abc[1][1] =500 # 此时我们修改了abc中下标为1的元素 [2,3,4] 但是[2,3,4] 是一个引用类型数据所以当我们修改这个时bcd也会变
print(bcd,'bcd')
print(abc,'abc')
print(abc is bcd) # false 因为是拷贝 is比较的是地址值

