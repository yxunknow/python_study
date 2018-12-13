#
# identifiers.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/13/18 18:39
#

# dir() return all attributes of an object

# print(dir('__builtins__'))


# _ receive a result but don't care about it

# for _ in (1, 2, 3, 5):
#     print('hello')

# integer
# python provides two integer types: integer and boolean
# integer is no length limitation but is limited by machine memory,
# bool is True or False
# and True = 1, False = 0 in integer
# some operations of integer
# // division but return an integer
# /  division but return an float
# x ** y, pow(x, y)
# x = 2
# y = 10
# print(x ** y)  # result is 1024

# x = 3
# y = 10
# print(y // x)  # result is 3

# divmod(a, b): return a tuple (a // b, a % b)
# print(divmod(y, x))

# pow(x, y, z) return (x ** y) % z, but more faster
# print(pow(2, 10, 1000))

# round(x, y): 按小数位多少位取整
# print(round(3.213614241, -3))

# base convert
# hex(): 16 ,0X
# bin(): 2  ,0B
# oct(): 8  ,0O

# three usages of dataType(), such as int()
# 1. assigned it to a new object reference: x = int(34), equals to x = 34
# 2. type cast: x = int('343'), convert a str object '343' to an int object
# 3. base convert, x = int('a4', 16), convert 'a4' to an int at 16 base

# .bit_length(), return bits number of an int
# print((12222222222222222222221111111113222222222222222444444421490894821908490214).bit_length())  # result is 243

# Boolean
# False and True are built-in boolean type in python
# logic operation on bool is short-circuit way

# Floating-point type
# float and complex and decimal, all three is immutable
# float: double-precision floating-point number
# float number can't use == to compare equality
# x = 5.4
# print(x)  # when output a float number, python use david gay's algorithm, this method can print fewest letter
# without losing any accuracy
# decimal is a high precision floating-point number type, but it is slower than flouting-point type
# from math import factorial
#
# print(factorial(1000))

# complex
# 4+13j

# decimal.Decimal
# x = decimal.Decimal('231412.4124213123')
# decimal is more accuracy than float, so it can safely use in financial area, but it is slower than float
# import decimal
# a = decimal.Decimal('23')
# b = decimal.Decimal('1.05')
# print(a / b)

# string

# long string
# longstr = str("this is a very very very very very very very very long,"
#               "but very very very very very very very very very very boring string")
#
# print(longstr)

# # index string
# positive index
#      0 1 2 3
# s = '中国无敌'
#     -4 -3 -2 -1
# negative index
# print(s[1], s[-3])

#　slice
# seq=s[index]
# seq=s[begin:end]
# seq=s[begin:end:step]
# s = 'abcdefghijklmnopqrstuvwxyz'
# s1 = s[0:25:2]
# print(s1)

# string operation
# *: replicate sting
# s = '123'
# s *= 4
# print(s)  #　s = 123123123123

# justify string
# s = 'china'
# sc = s.center(10, '*')
# sl = s.ljust(10, '*')
# sr = s.rjust(10, '*')
# print(sc)
# print(sl)
# print(sr)

# format string
