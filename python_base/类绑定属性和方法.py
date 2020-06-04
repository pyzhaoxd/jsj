class Student():
    pass

s = Student()
s.name = 'zhaoxd'
print(s.name)

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

#给一个实例绑定的方法，对另一个实例不起作用
s2 = Student()
# s2.set_age(25)



#给class绑定属性方法后，所有实例可调用
def set_score(self,score):
    self.score = score
#
Student.set_score = set_score
s2.set_score(100)
print(s2.score)
# s4.set_age2(99)
# print(s4.core)


#使用__slots__

#如果我们想要限制实例的属性怎么办，比如只能对Student实例添加name和age属性

class Student1(object):
    __slots__ = ('name','age') #用tuple定义允许绑定的属性名称


s7 = Student1()
s7.name = 'zhaoxd'
s7.age = 12    #绑定属性name和age
print(s7.name)
print(s7.age)
#s7.score = 18 #绑定未在限制内的属性到class
#print(s7.score)


#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class graduateStudent(Student1):
    pass

g = graduateStudent()
g.score = 99
print(g.score)

#除非在子类中也定义__slots__，这样,子类实例允许定义的属性就是自身的__slots__，加上父类的__slots__