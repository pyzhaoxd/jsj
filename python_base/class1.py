#继承
class one:
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
#任何形如 __spam 的标识（前面至少两个下划线，后面至多一个），被替代为 _classname__spam ，去掉前导下划线
#名称重整是有助于子类重写方法，而不会打破组内的方法调用。例如:
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

class Employee:
    pass

john = Employee() # Create an empty employee record
# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print(john.name)


#异常也是类