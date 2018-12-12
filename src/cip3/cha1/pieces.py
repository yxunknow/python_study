# data type
# int : there is no length limitation on integer, but it limited by  machine memory
# str : immutable data

# object reference
# an object reference points on a memory address
# type check: type() or isinstance()

# collection data types
# tuple: immutable collection
# list: mutable collection
# tuple or list stores references of items, not value of items directly
# tuple and list is an object too, this is the reason that tuple or list can be nested
# len(): return length of item as an int, the item should be sized type. such as str, list, tuple or dict

# logical operations
# is: identity operator, compare by memory address
# check weather two objects are same reference(both references point on a same memory address)
# the most common use of 'is' is to compare a data item with built-in null object None,
# such as >> a is None or >> b is not None
# a = 2
# b = None
# a is None  # False
# b is None  # True
# a is not None  # True
# ---=---=---=---=---=---=
# comparision operators: compare by value
# < less than
# <= less than or equal to
# == equal to
# != not equal to
# >= greater than or equal to
# > greater than
# chain comparision operators use
# 0 <= a <= 10
# x = 8
# 0 <= x <= 10  # True
# membership operator
# for data types that are sequences or collections such as list, string, tuple
# in: check weather a item is in an object
# not in: check weather a item is not in an object
# myLanguageSkin = ['Java', 'Kotlin', 'Angular', 'JS']
# newLanguage = 'Python'
# if newLanguage in myLanguageSkin:
#     print('you have python skills')
# else:
#     print('you have not grasp python yet')
# in will become slow when used on large lists or tuples, because it uses linear search algorithm
# but in is very fast when used on dicts or sets
# when in used on strings, it can search substrings or characters
# ---=---=---=---=---=---=---=
# logical operators
# and: return last operand when used on non-boolean data
# or: return first operand when used on non-boolean data
# not: return boolean

# control flow statements
# False default value
# str: ''
# int: 0
# list: []
# set: set()
# dict: {}
# tuple: ()
# if
# if boolean-expression1:
#     ...
# elif boolean-expression2:  #(elif segments can be zero or more)
#     ...
# elif boolean-expression3:
#     ...
# else:  #(else segment is optional)
#     ...
# pass: a key-word presents do nothing in a code block
# while
# while boolean-expression:
#     ...
# for
# for variable in iterable:
#     ...
# exception handling
# try:
#     x = input('input a number:')
#     x = int(x)
#     print('Get a number:{}'.format(x))
# except ValueError as err:
#     print(err)
#     print('Your input is not a valid number')
# finally:
#     # do finally is optional

# arithmetic operators
# +: addition
# -: subtraction
# *: multiplication
# /: division, return float value
# //: division, return integer value
# +=: addition and assignment
# *=: multiplication and assignment
# -=: subtraction and assignment
# /=: division and assignment
# + can be used on list, string, etc.
# for list, the second operand must be iterable, and + add all iterated item into list

# input/output
# input(): accept user's input
# print(): print data to console by default
# print redirection
# print("hello, print is redirected into a file")
# python3 ./pieces.py > print.txt# data type
# int : there is no length limitation on integer, but it limited by  machine memory
# str : immutable data

# object reference
# an object reference points on a memory address
# type check: type() or isinstance()

# collection data types
# tuple: immutable collection
# list: mutable collection
# tuple or list stores references of items, not value of items directly
# tuple and list is an object too, this is the reason that tuple or list can be nested
# len(): return length of item as an int, the item should be sized type. such as str, list, tuple or dict

# logical operations
# is: identity operator, compare by memory address
# check weather two objects are same reference(both references point on a same memory address)
# the most common use of 'is' is to compare a data item with built-in null object None,
# such as >> a is None or >> b is not None
# a = 2
# b = None
# a is None  # False
# b is None  # True
# a is not None  # True
# ---=---=---=---=---=---=
# comparision operators: compare by value
# < less than
# <= less than or equal to
# == equal to
# != not equal to
# >= greater than or equal to
# > greater than
# chain comparision operators use
# 0 <= a <= 10
# x = 8
# 0 <= x <= 10  # True
# membership operator
# for data types that are sequences or collections such as list, string, tuple
# in: check weather a item is in an object
# not in: check weather a item is not in an object
# myLanguageSkin = ['Java', 'Kotlin', 'Angular', 'JS']
# newLanguage = 'Python'
# if newLanguage in myLanguageSkin:
#     print('you have python skills')
# else:
#     print('you have not grasp python yet')
# in will become slow when used on large lists or tuples, because it uses linear search algorithm
# but in is very fast when used on dicts or sets
# when in used on strings, it can search substrings or characters
# ---=---=---=---=---=---=---=
# logical operators
# and: return last operand when used on non-boolean data
# or: return first operand when used on non-boolean data
# not: return boolean

# control flow statements
# False default value
# str: ''
# int: 0
# list: []
# set: set()
# dict: {}
# tuple: ()
# if
# if boolean-expression1:
#     ...
# elif boolean-expression2:  #(elif segments can be zero or more)
#     ...
# elif boolean-expression3:
#     ...
# else:  #(else segment is optional)
#     ...
# pass: a key-word presents do nothing in a code block
# while
# while boolean-expression:
#     ...
# for
# for variable in iterable:
#     ...
# exception handling
# try:
#     x = input('input a number:')
#     x = int(x)
#     print('Get a number:{}'.format(x))
# except ValueError as err:
#     print(err)
#     print('Your input is not a valid number')
# finally:
#     # do finally is optional

# arithmetic operators
# +: addition
# -: subtraction
# *: multiplication
# /: division, return float value
# //: division, return integer value
# +=: addition and assignment
# *=: multiplication and assignment
# -=: subtraction and assignment
# /=: division and assignment
# + can be used on list, string, etc.
# for list, the second operand must be iterable, and + add all iterated item into list

# input/output
# input(): accept user's input
# print(): print data to console by default
# print redirection
# print("hello, print is redirected into a file")
# $ python3 ./pieces.py > print.txt
# input redirection
# while True:
#     try:
#         line = input()
#         if line:
#             print('receive line:', line)
#     except EOFError:
#         break
# $ python3 ./pieces.py < print.txt

# creating and calling functions
import random
x = random.choice(['apple', 'xiaomi', 'huawei', 'microsoft'])
print(x)