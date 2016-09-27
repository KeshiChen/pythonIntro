i = 100
print(i)
i = 1.1
print(i)
i = 'python 是弱类型,解释型语言'# That's NOT OK in JAVA/C/C++
print(i)

# 不是指针的ref
a = 'ABC'
b = a
print(a)
print(b)
b = 'DEF'
print(a)
print(b)

c = 'ABC'
d = c
c = 'XYZ'
print(c)
print(d)

list_ = [1,2,3]

def changeList(l):
    l[0] = 100

changeList(list_);

print(list_)



