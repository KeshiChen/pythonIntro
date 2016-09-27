#单行注释
'''
可以换行
的注释
'''
def hello(you):
    print('Hello ' + you + '!')

print(__name__)

if __name__ == '__main__':
    hello('world')
    hello('Jane')
    hello('Michael')
