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

# list.insert(i, x)
# 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x)
# 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x)。
x.insert(0,13)
print(x)
