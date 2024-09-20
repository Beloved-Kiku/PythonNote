# 字典是python中一种有序 以kv对形式存储的数据类型 它是可更改的但是不允许重复
# 在python 3.6以后在底层帮我们记录kv录入的顺序 但是字典还是是无序的 这也是我们遍历为什么看从前到后依次打印
# 字典中的数据类型可以是任意数据类型
#创建字典的各种方式
#1.直接创建
person = {"name":"张三","age":18,"gender":"男"}
print(type(person)) #<class 'dict'>
#2.通过dict()函数创建
person2 = dict(name="李四",age=19,gender="女")
print(type(person2)) #<class 'dict'>
#3.通过zip()函数创建
person3 = dict(zip(["name","age","gender"],["王五",20,"男"]))
print(type(person3)) #<class 'dict'>
#4.通过fromkeys()函数创建
person4 = dict.fromkeys(["name","age","gender"],'Nginx')   #创建一个键值对，键为"name","age","gender"，值为"未知"
print(type(person4),person4) #<class 'dict'>
#5.使用可迭代对象创建
person5 =dict([[1,200],[2,18],[3,0],('code','python')])
print(person5)
#字典访问方法和js大同小异
JsDict = {"one":'html',"two":'css',"three":'js','four':'ajax','five':'vue','six':'react'}
print(JsDict["one"]) #html
print(JsDict.get("one")) #html
#访问字典中的key
print(JsDict.keys()) #dict_keys(['one', 'two', 'three', 'four', 'five', 'six'])
#访问字典中的value
print(JsDict.values()) #dict_values(['html', 'css', 'js', 'ajax', 'vue', 'react'])
#访问字典中的key-value对
print(JsDict.items()) #dict_items([('one', 'html'), ('two', 'css'), ('three', 'js'), ('four', 'ajax'), ('five', 'vue'), ('six', 'react')])
#字典的更新
#通过key寻找到值进行更新 覆盖原来到值
JsDict["one"] = "css"
#通过update()方法更新 update参数必须是字典，或者具有键：值对的可迭代对象。
JsDict.update({"one":"html","two":"css","three":"js","four":"ajax","five":"vue","six":"react"})
#字典的删除
#通过del关键字删除 del也可以直接删除整个字典
del JsDict["one"]
#通过pop()方法删除 pop()方法会返回被删除的值 pop方法可以接受两个参数第一个参数是key，第二个参数是默认值，如果key不存在，则返回默认值
print(JsDict.pop("two")) #css
#通过popitem()方法删除 popitem()方法会返回一个元组，元组中包含两个元素，第一个元素是键，第二个元素是值
print(JsDict.popitem()) #('six', 'react')
#通过clear()方法清空字典
JsDict.clear()
JsDict = {"one":'html',"two":'css',"three":'js','four':'ajax','five':'vue','six':'react'}
#字典的遍历
# 当我们在对字典进行遍历时 我们不能去对字典进行添加或者删除 这样会影响字典的长度从而造成报错
for key in JsDict:
    print(key,JsDict[key]) #one html two css three js four ajax five vue six react
    #item 方法如果kv都是可hash的那么item返回的对象也是可哈希对象 也是一个类set对象
for key,value in JsDict.items():
    print(key,value) #one html two css three js four ajax five vue six react
    #keys方法返回的是一个类set对象  我们可以用来做set集合运算
for key in JsDict.keys():
    print(key) #one two three four five six
for value in JsDict.values():
    print(value) #html css js ajax vue react

