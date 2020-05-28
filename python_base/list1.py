squares = [1, 4, 9, 16, 25]
print(squares)

#就像字符串(以及其它所有内建的 序列 类型)一样，列表可以被索引和切片:
print(squares[-0])
print(squares[-1])
print(squares[-3])
print(squares[:])
print(squares + [30,35,40])
#不可变的 字符串，列表是 可变的，它允许修改元素:

cubes = [1,2,3,4,5]
cubes[3] = '7'
print(cubes)

#使用 append() 方法 （后面我们会看到更多关于列表的方法的内容）在列表的末尾添加新的元素:
cubes.append(216)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)

#内置函数 len() 同样适用于列表:
letters = ['a', 'b', 'c', 'd']
print(len(letters))


a = [1,2,3,[4,9]]
print(id(a))
b = a[:]
print(id(b))
a[3][0]=7
print(id(a))
a[2] = 5
print(id(b))
print(a)
print(b)

a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0][1])

a, b = 0, 1
while b < 10:
    print(b)
    a,b = b, a+b