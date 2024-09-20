# 列表 列表基本格式   ListName =   [元素1,元素2,元素3,...]
# 列表可以存储任意类型,列表可以存储任意多个元素的数据
from doctest import debug

from pandas.io.formats.format import return_docstring
NameList =['beloved','jack','tom','lucy']
#列表的增删改查
# 增加元素  append()  在列表末尾添加元素     insert()  在指定位置添加元素 extend()  在列表末尾添加多个元素
NameList.append('lily')
print(NameList,'添加后的列表')
NameList.insert(1,'lucy')   #在指定位置添加元素
print(NameList,'指定位置添加元素后的列表')
NameList.extend(['lucy','tom'])  #在列表末尾添加多个元素
print(NameList,'在列表末尾添加多个元素后的列表')
# 删除元素  remove()  删除指定元素  pop()  删除指定位置的元素   clear()  清空列表
NameList.remove('lucy')  #删除指定元素若元素有重复则删除第一个
print(NameList,'删除指定元素后的列表')
NameList.pop(1)  #删除指定位置的元素
NameList.pop()  #删除指定位置的元素 若不给参数则选择删除最末尾的一个
print(NameList,'删除指定位置的元素后的列表')
NameList.clear()  #清空列表
print(NameList,'清空列表后的列表')
# 列表排序
# sort()  排序  reverse()  反转
NameList =['beloved','jack','tom','lucy']
NameList.sort()  #排序    默认从小到大排序    若想从大到小排序则可以加参数reverse=True
print(NameList,'排序后的列表')
NameList.reverse()  #反转
print(NameList,'反转后的列表')
# 列表切片  列表名[开始位置:结束位置:步长]  左闭右开区间
print(NameList[0:3:1],'列表切片')
# index 查找元素位置  可设置查找的起始位置 count查找元素个数 都需要从左到右依次查找效率低 O(n)时间复杂度
print(NameList.index('tom'),'查找元素位置')
print(NameList.count('tom'),'查找元素个数')
List = [range(1,1000000)]
# 遍历List
for i in List[0]:
    if List[0].index(i)%2==0:
        print(i)
#append的效率  O(1)时间复杂度 一般情况下效率高 若列表不够存储则需要进行扩容若内存连续空间不够则需要等待垃圾回收此时append的效率将会变低
#insert的效率  O(n)时间复杂度  每次插入都需要移动元素 效率很低
List.insert(-1,'nginx')
print(List)

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