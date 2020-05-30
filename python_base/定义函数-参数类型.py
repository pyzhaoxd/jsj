def test(n):
    '''test funciton'''
    while n < 5:
        print("num is lt 5" )
        return n
        break
    else:
        print("num is gt 5")

# test(4)

#关键字 def 引入了一个函数 定义。在其后必须跟有函数名和包括形式参数的圆括号。函数体语句从下一行开始，必须是缩进的。
#函数 调用 会为函数局部变量生成一个新的符号表。确切的说，所有函数中的变量赋值都是将值存储在局部符号表。
# 变量引用首先在局部符号表中查找，然后是包含函数的局部符号表，然后是全局符号表，最后是内置名字表。
# 因此，全局变量不能在函数中直接赋值（除非用 global 语句命名），尽管他们可以被引用。

#一个函数定义会在当前符号表内引入函数名。函数名指代的值（即函数体）有一个被 Python
# 解释器认定为 用户自定义函数 的类型。 这个值可以赋予其他的名字（即变量名），然后它也可以被当做函数使用
# 这可以作为通用的重命名机制:

# a = test
# print(a(4))

#如果你使用过其他语言，你可能会反对说：fib 不是一个函数，而是一个方法，因为它并不返回任何值。
# 事实上，没有 return 语句的函数确实会返回一个值，虽然是一个相当令人厌烦的值（指 None ）。
# 这个值被称为 None （这是一个内建名称）。如果 None 值是唯一被书写的值，
# 那么在写的时候通常会被解释器忽略（即不输出任何内容）。如果你确实想看到这个值的输出内容，请使用

def test1(n):
    '''test funciton'''
    result = []
    while n < 5:
        result.append(n)
        print("num is lt 5")
        return result

    else:
        print("num is gt 5")
        return result


b = test1(4)
print(b)

# 默认参数值
def defaultfunc(name,age=12,body=15):
        if name == 'zhaoxd':
            print("hello",name)
        elif age > 12:
             print(name,"age gt default",age)
        elif body < 15:
            print(name,"body lt default",body)
        else:
            print("name input error")


#函数调用
defaultfunc("zhaoxd")
defaultfunc("yangxueli")
defaultfunc("jsj",age=16)
defaultfunc(name="123",body=12)

i = 5
def f(arg=i):
    print(arg)

i = 6
print(f())
#重要警告: 默认值只被赋值一次。这使得当默认值是可变对象时会有所不同，比如列表、
# 字典或者大多数类的实例。例如，下面的函数在后续调用过程中会累积（前面）传给它的参数:

def f1(a, L=[]):
    L.append(a)
    return L

print(f1(1))
print(f1(2))
print(f1(a = 3))


#如果你不想让默认值在后续调用中累积，你可以像下面一样定义函数:
def f2(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L


#关键字参数，形如 keyword = value。例如，以下的函数:
def parrot(voltage,state='a stiff',action='voom',type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
#接受一个必选参数 (voltage) 以及三个可选参数 (state, action, 和 type)。可以用以下的任一方法调用:
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


#在函数调用中，关键字的参数必须跟随在位置参数的后面。传递的所有关键字参数必须与函数接受的某个参数相匹配
#它们的顺序并不重要。这也包括非可选参数（例如 parrot(voltage=1000) 也是有效的）。任何参数都不可以多次赋值


def function(a):
    pass

# function(0,a=0)

#引入一个形如 **name 的参数时，它接收一个字典（参见 Mapping Types — dict ）
# 该字典包含了所有未出现在形式参数列表中的关键字参数。这里可能还会组合使用一个形如 *name （
# 下一小节详细介绍） 的形式参数，它接收一个元组（下一节中会详细介绍），
# 包含了所有没有出现在形式参数列表中的参数值（ *name 必须在 **name 之前出现）
# 例如，我们这样定义一个函数:

def cheeseshop(kind,*args,**kwargs):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in args:
        print(arg)
    print('-' * 40)
    keys = sorted(kwargs.keys())
    for kw in keys:
        print(kw,':',kwargs[kw])
#它可以像这样调用:
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#注意在打印关键字参数之前，通过对关键字字典 keys() 方法的结果进行排序，
# 生成了关键字参数名的列表；如果不这样做，打印出来的参数的顺序是未定义的


#可变参数列表
#通常，这些 可变 参数是参数列表中的最后一个，因为它们将把所有的剩余输入参数传递给函数。
# 任何出现在 *args 后的参数是关键字参数，这意味着，他们只能被用作关键字，而不是位置参数:

def concat(*args,sep='/'):
    return sep.join(args)

print(concat('etc','http','http.conf'))
print(concat("earth", "mars", "venus", sep="."))

#参数列表的分拆
#另有一种相反的情况: 当你要传递的参数已经是一个列表，但要调用的函数却接受分开一个个的参数值。
# 这时候你要把已有的列表拆开来。例如内建函数 range() 需要要独立的 start，stop 参数。
# 你可以在调用函数时加一个 * 操作符来自动把参数列表拆开:

print(list(range(3,6)))
args = [3,6]
print(list(range(*args)))

def list1(number,number1,number2):
    print(number)
    print(number1)
    print(number2)

a = [1,2,3]
print(list1(*a))

#以同样的方式，可以使用 ** 操作符分拆关键字参数为字典
def parrot(voltage,state='a stiff',action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(parrot(**d))




a = ['a','b']
c = ['e','f']
print(list(zip(a,c)))
print(list(enumerate(a)))

#Lambda
#通过 lambda 关键字，可以创建短小的匿名函数。这里有一个函数返回它的两个参数的和：
#lambda a, b: a+b。 Lambda 形式可以用于任何需要的函数对象。出于语法限制，
# 它们只能有一个单独的表达式。语义上讲，它们只是普通函数定义中的一个语法技巧。类似于嵌套函数定义，lambda 形式可以从外部作用域引用变量:
def make_incrementor(n):
    return lambda x: x + n
j = make_incrementor(42)
print(j(0))
print(j(1))
print(j(2))
#上面的示例使用 lambda 表达式返回一个函数。另一个用途是将一个小函数作为参数传递:
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1]) #value作为排序指标
print(pairs)

