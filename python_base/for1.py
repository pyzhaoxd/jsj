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

#如果你只是打印一个序列的话会发生奇怪的事情:
print(range(10))