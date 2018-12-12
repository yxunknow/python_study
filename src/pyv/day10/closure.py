# closure is nested function
# inner function use variables of outer function
# def outer():
#     a = 1
#     def inner(x):
#         print(x + a)
#     return inner
#
# outer()(24)

import urllib

from urllib.request import urlopen

c = urlopen('http://mevur.bennkyou.top:8848/dasheng?page=1').read()
print(str(c))
