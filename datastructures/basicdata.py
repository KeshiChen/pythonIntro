# Python list

list_ = list((1,2,3)) # same as ["zhang wei", 123, 1.21]


for ele in list_:
    print(ele,end='');

print();

# last element
print(list_[-1])


# tuple

t = ();#immutable
t = (1,2,['a','b']);

print(t)

t[2][0] = 1;

print(t)

#Error:
#t[2] = "c";



# # Non ordering datastructure
# # dictionary
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d['Michael'] #Access value
# d['Bob'] = 75
# d['Linus'] = 10
#
# print('Bob' in d)
# print('MMM' in d)
#
# d.pop('Bob')
#
# #set
# #duplicate eliminate
#
# s = set([1, 2, 3])
# s2 = set([1,2])
# s3 = set([3,5])
#
# print(s-s2)
# print(s3.union(s))
# s.add(4)
# s.remove(4)