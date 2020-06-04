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

