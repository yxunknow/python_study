#
# set.py
# Created in Intelij IDEA
# 
# shallow and deep copy in set
# 
# @author Mevur
# @date 12/06/18 18:22
# 

# set is a mutable data type, but elements in set must be immutable,
# set is disordered, and there is no same element in set.

s = set({1, 2, 3})
# s1 = {1, 3, 9, [1, 2, 3], {'ad': '23'}}
# list is unhashable


# insert
s.add('232')

# update
# add an iterable object into set
s.update('232wda2')

# delete
# 1. random delete an element and return deleted-element
deleteValue = s.pop()
# 2. delete element, if element is not in set, will produce an error
s.remove('232')
# 3. clear
# set a set as empty, empty set is 'set()'
# s.clear()

# 4. del
# del s
# delete a set from memory

# query
# for e in s:

# set operation
# 1. intersection
s1 = {2, 3, 1}
s2 = {2, 3, 5}
s3 = s1 & s2
# s3 = s1.intersection(s2)

# union
s4 = s1 | s2
s5 = s1.union(s2)

# difference
s7 = s1 ^ s2
s8 = s1.symmetric_difference(s2)

# minus
s9 = s1 - s2
s10 = s1.difference(s2)

# type cast
li = [1, 2, 3, 2, 4, 5, 1, 2]
# list to set
se = set(li)
# set to list
li = list(se)

# frozenset
fs = frozenset({'2', 2, '4'})
print(fs)

for x in fs:
    print(x)


