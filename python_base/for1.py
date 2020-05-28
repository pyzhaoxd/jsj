word = ['cat','window','defenesstrate']
for w in word:
    print(w,len(w),type(w))

#在迭代过程中修改迭代序列不安全（只有在使用链表这样的可变序列时才会有这样的情况）
# 如果你想要修改你迭代的序列（例如，复制选择项），你可以迭代它的复本。使用切割标识就可以很方便的做到这一点
for w in word[:]:
    if len(w) > 6:
        word.insert(0,w)
        print(word)