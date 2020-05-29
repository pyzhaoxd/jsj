word = ['cat','window','defenesstrate']
for w in word:
    print(w,len(w),type(w))

#在迭代过程中修改迭代序列不安全（只有在使用链表这样的可变序列时才会有这样的情况）
# 如果你想要修改你迭代的序列（例如，复制选择项），你可以迭代它的复本。使用切割标识就可以很方便的做到这一点
for w in word[:]:
    if len(w) > 6:
        word.insert(0,w)
        print(word)

#range() 函数
for i in range(5):
    print(i)

print(range(5,10))
print(range(0,10,3))
print(range(-10,-100,-30))

#需要迭代链表索引的话，如下所示结合使 用 range() 和 len()
a = ['Mary', 'had', 'a', 'little', 'lamb']
print(len(a))
for i in range(len(a)):
    print(i,a[i])

#不过，这种场合可以方便的使用 enumerate()，请参见 循环技巧。
#循环技巧
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)

#在序列中循环时，索引位置和对应值可以使用 enumerate() 函数同时得到:
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

#同时循环两个或更多的序列，可以使用 zip() 整体打包:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q ,a in zip(questions,answers):
    print('what is you {0}? It is {1},'.format(q,a))

#需要逆向循环序列的话，先正向定位序列，然后调用 reversed() 函数:
for i in reversed(range(1,10,2)):
    print(i)

#要按排序后的顺序循环序列的话，使用 sorted() 函数，它不改动原序列，而是生成一个新的已排序的序列:
#set 去重
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

#如果你只是打印一个序列的话会发生奇怪的事情:
print(range(10))

#5.7. 深入条件控制
#while 和 if 语句中使用的条件不仅可以使用比较，而且可以包含任意的操作。
#比较操作符 in 和 not in 审核值是否在一个区间之内。操作符 is 和 is not 比较两个对象是否相同；
# 这只和诸如列表这样的可变对象有关。所有的比较操作符具有相同的优先级，低于所有的数值操作。

#比较操作可以传递。例如 a < b == c 审核是否 a 小于 b 并且 b 等于 c。

#比较操作可以通过逻辑操作符 and 和 or 组合，比较的结果可以用 not 来取反义。
# 这些操作符的优先级又低于比较操作符，在它们之中，not 具有最高的优先级，
# or 优先级最低，所以 A and not B or C 等于 (A and (notB)) or C。当然，括号也可以用于比较表达式。

print(list(range(5)))