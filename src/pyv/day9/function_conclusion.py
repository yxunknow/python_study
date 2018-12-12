#
# function_conclusion.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/11/18 20:39
# 

# parameter
# no parameter
#   def fun()
#   fun()
# single paramter
#   def fun(param)
#   fun(param)
# multiple parameters
#   def fun(param1, param2)
#   fun(p1, p2)

# function support named parameter
def fun(name, age):
    print('name:{}\t\tage:{}'.format(name, age))

fun(name='cheng', age=23)

# default value
# default value parameter can be omitted
def show(name, age, sex='男'):
    print('name:{}, age:{}, sex:{}'.format(name, age, sex))

show(name='chengpiao', age=23)
show(name='cheng', age=23, sex='女')

# dynamic parameter
# 参数个数不确定
def sum(*args):
    res = 0
    for arg in args:
        if type(arg) == int:
            res += arg

    return res

print(sum(1,2, 4, '23', 123))

# multiple named parameter
# accepted key-value parameter
def kw(**args):
    for i in args.items():
        print(i)

kw(a = 2, b = 3, name = 'cheng')

# *args: receive parameters as a tuple, 按位置传参数
# **args: receive parameters as a dict， 按名字传参数

# super combine
def superf(*args, **kwargs):
    pass

# parameter orders
def funex(*args, default=1, **kwargs):
    '''
    feature description
    :param args: args description
    :param default:
    :param kwargs:
    :return: return description
    '''
    pass

# pass dynamic parameters
l = [1, 3, 4, 9, 10, 23]
print(sum(*l))