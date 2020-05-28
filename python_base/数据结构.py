#Python 的列表数据类型包含更多的方法。这里是所有的列表对象方法：

#list.append(x)
#把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]
x = [1,2,3,4]
print(len(x))
x.append(5)
print(x)


#list.extend(L)
#将一个给定列表中的所有元素都添加到另一个列表中，相当于 a[len(a):] = L
l = [9,10]
x.extend(l)
print(x)
