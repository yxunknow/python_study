li = ['alex', 'python', 'java', 'js', 'kotlin']
alex = li[0]
# use index read element in list
print(alex)

# slice
# return a list
l3 = li[0:3]

# crud in list
# insert
# 1 append: append an object to end
li.append('json')
# exercise
while 1: 
    #input data to s
    username = input('input username')
    if username.strip().upper == 'Q':
        break
    else:
        li.append(s)

# 2 insert: insert an object at position
li.insert(3, 'type')
# 3 extend: append object, the object must be iterable
li.extend('232')
li.extend([1, 2, 3])

# delete
# 1. pop: delete element with index and return element be deleted
# when index is None, the last element will be deleted
deletedValue = li.pop(1)
# 2 remove: remove by value
li.remove('java')
# 3 clear: clear list
li.clear()
# 4 del: delete list from memory
del li
# delete a range of data
del li[2:4]

# update [index-based write and read]
# delete old value and insert new value
li[0] = 'alice'
# range update
# del range data and insert new data, new data
# should be iterable
li[0:2] = 'android'

# read
for ele in li: 
    print(ele)
# range data
e = li[0]
e2 = li[0:2]

# len: return size of list
len = len(li)
# count: count times in list of a value
count = li.count('kotlin')
# index of element
index = li.index('java')
index = li.index('java', 2, 4)
# sort
nums = [1, 4, 5, 2, 9 ,3]
# asc order
nums.sort()
# desc order
nums.sort(reverse=True)
# sort as asc order and reverse
nums.sort().reverse()
