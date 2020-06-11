import logging
logging.basicConfig(filename='test.log',level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
       a = bar('0')
    except Exception as e:
        logging.info(e)
    else:
        return a

print(main())
print('end')