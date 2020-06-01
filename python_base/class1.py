#继承
class one():
    def ___init__(self,name):
        self.name = name

    def alex(self):
        return self.name


class two(one):
    def __init__(self,age):
        self.age = age

    def ages(self):
        return self.age
a = one()
a.name = 'zhaoxd'
print(a.name)
print(a.alex())

b = two(one)
b.age = 18
print(b.age)


#私有变量
