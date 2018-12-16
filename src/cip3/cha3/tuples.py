#
# tuples.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/16/18 17:31
# 
# a tuple is an ordered sequence of zero or more items, and is an immutable type.
# index of tuple
#             tu[-4]   tu[-3]  tu[-2]  tu[-1]
# tu = tuple('venus', 'mars', 'earth', 'sun')
#             tu[0]    tu[1]   tu[2]   tu[3]
# tuple is a collection of references

# method
# count(x): return count of x occurs in tuple
# index(x): return first-most position of x in tuple, or raises a valueError if the x is't
#           in tuple

# tu = ('china', 'is', 'blue')
# print(tu)
#
# tu *= 3
# print(tu)  # result is ('china', 'is', 'blue', 'china', 'is', 'blue', 'china', 'is', 'blue')
#
#
# china = tu[0]  # china = tu[-3]
# print(china)

# below declaration is not a tuple
# type(tu) will output <class 'int'>
# tu = (1)
# print(type(tu))

# below declaration is a tuple
# so if we want to declare a single-item tuple, the comma is needed
# tu = (1,)
# print(type(tu))

# multi-layers nested tuple can lead confusions
# the solution is giving names to particular index positions
# TRAIN_NUMBER, DATE, SEAT_NUMBER = (0, 1, 2)  # a tuple is unpacked to left-hand variables
# CARRIAGE, SEAT = (0, 1)
# ticket = ('G8586', '2018-12-16', ('12车', '8F'))
# print(ticket[SEAT_NUMBER][CARRIAGE])  # output is '12车'
# this trick creates too many variables and makes code ugly

# named tuples
# a named tuple can refer item by name as same with by index
# from collections import namedtuple
# Sale = namedtuple('Sale', 'prodctid customid date quantity price')
# sales = list()
# sales.append(Sale(1, 2314, '2018-12-16', 20, 100))
# print(sales)
# aSale = sales[0]
# customIdOfASale = aSale.customid
# print(customIdOfASale)
# namedTuple._asdict() return named tuple as key-value pairs
# print(sales[0]._asdict())



