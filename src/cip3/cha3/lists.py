#
# lists.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/16/18 18:27
# 


# list is an ordered of zero or more object references, and is mutable.

# unpack operation of list
# first, *rest = [9, 2, '共', '识']
# # first = 2, rest = [2, '共', '识']
# print(first, rest)

# first, *mid, last = [9, 2, '共', '识']
# # first = 9, mid = [2, '共'], last = '识'

# methods
districts = ['nanan', 'yuzhong', 'yubei', 'jiangbei', 'beibei', 'jiangjin']

# pop(): delete the last item and return it
# print(districts.pop())  # delete jiangjin
# print(districts.pop())  # delete beibei
# print(districts.pop())  # delete jiangbei

# pop(index): delete item at index and return it
# if the index is not in range, will raise IndexError
# print(districts.pop(-1))  # delete jiangjin
# print(districts.pop(4))  # delete beibei
# print(districts.pop(10))  # raises IndexError

# remove(x): delete left-most item which value is x, no return value
# if x is not found, will raise ValueError
# districts.remove('jiangjin')  # delete jiangjin
# districts.remove('dadukou')  # raises ValueError


