#
# method.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/11/18 19:31
# 

# len
s = '中国china'

# declare a function
def slen(s: str):
    '''
    return length of a string
    :param s: string
    :return: length of s
    '''
    length = 0
    for c in s:
        length += 1
    return length

# call function
l = slen(s)
print(l)

# return value
# no return value (return None)
#   no return statement
#   return
#   return None
# return single value
#   return object
# return multiple value
#   return object, object
#   return data is a tuple, but destruct to variable


# all iterable object can be destructed into variables
