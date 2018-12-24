#
# sets.py.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/17/18 20:01
# 

# set is a collection data type
# only hashable objects can be added to a set
# hashable objects are which hava __hash__() method
# all built-in immutable data types, such as float, frozenst, int, str and tuple
# , are hashable. dict, list, and set are not hashable.

# set is an unordered collection of zero or more object references that refer to hashable object.
# set is mutable.

# s = {7, 'veil', 0, -29, ('x', 11), 'sun', frozenset({8, 4, 7}), 913}
# print(s)

# comprehension
# { expression for item in iterable}
# { expression for item in iterable if condition}
# html = { x for x in files if x.lower().endsWith('htm', 'html')

# frozenset
# a frozen set is an immutable date type
# frozen = frozenset({1, 2, 3})

# mapping data type
# mapping type is store key-value pairs and provides methods to read keys or values.
# since python 3.1, there are three mapping types: dict, collections.defaultdict, and collections.OrderedDict
# dict and collections.defaultdict are unordered, but collections.OrderedDict is ordered
# only hashable type can be key of maps, but there is no limitation on values

# dictionaries
# dict is an unordered collection of zero or more key-value pairs,
# keys are object references refer to hashable types and values are object references refer to any types.
# dictionaries are mutable

# ordered-dictionaries
from collections import OrderedDict

odict = OrderedDict()
odict[1001] = 'backup'
odict[2031] = 'shutdown'
odict[1023] = 'gib byte'
print(odict)

