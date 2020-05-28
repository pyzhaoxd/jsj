
# if 语句
x = int(input("please enter an integer:"))
if x <= 0:
    print("Negative changed to zero")
else:
    print("This is number gt 0")

y = int(input("Please enter an integer: "))

if y <= 0:
    print('Negative changed to zero')
elif y == 0:
    print('Zero')
elif y == 1:
    print('Single')
else:
    print('More')