for n in range(2,10):
    print('return',n)
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals', x, '*', x)
            break
    else:
        print(n, 'is a prime number')


#[x for x in range(10) if x % 2 == 0 ]
#{x for x in range(10) if x % 2 == 0 }
#(Yes, 这是正确的代码。看仔细：else 语句是属于 for 循环之中， 不是 if 语句。)

#与循环一起使用时，else 子句与 try 语句的 else 子句比与 if 语句的具有更多的共同点：
# try 语句的 else 子句在未出现异常时运行，循环的 else 子句在未出现 break 时运行。
# 更多关于 try 语句和异常的内容，请参见 异常处理。


#continue 语句是从 C 中借鉴来的，它表示循环继续执行下一次迭代:
print(list(range(2,10)))
for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number",num)
        continue
    print("Found a number", num)


#pass语句
#pass 语句什么也不做。它用于那些语法上必须要有什么语句，但程序什么也不做的场合，例如:
while True:
    pass