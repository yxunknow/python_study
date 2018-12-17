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

# operation on list
# insert
# append(x), append an item at the end of a list
# insert(index, element), insert element at index
# districts[1:1] = ['dadukou']  # districts.insert(1, 'dadukou')
# districts.insert(1, 'dakukou')
# print(districts)

# delete
# districts[1:2] = []  # delete districts[1], 'yuzhong'
# del districts[1:2]  # delete districts[1], 'yuzhong'
# print(districts)


# comprehensions
# range(start, end, step) return a range
# li = list(range(0, 10))
# print(li)
# leaps = []
# get all leap year from 1900 to 2022
# for year in range(1900, 2022, 4):
#     if (year % 4 ==0 and year % 100 !=0) or (year % 400 == 0):
#         leaps.append(year)
#
# print(leaps)
# list comprehensions
# 1
# return year between 1900-2021
# years = [y for y in range(1900, 2022)]
# years = list(range(1900, 2022))
# print(years)
# 2 with condition
# leaps = [y for y in range(1900, 2022, 4) if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]
# print(leaps)

# comprehension nested
# sex = 'MF'
# size = 'SMLX'
# color = 'WGB'
# tags = []
# for g in sex:
#     for s in size:
#         if g == 'F' and s == 'X':
#             continue
#         for c in color:
#             tags.append('sex:{} size:{} color:{}'.format(g, s, c))
# print(tags)
# below code is less shorter
# tags = ['sex:{} size:{} color:{}'.format(g, s, c) for g in sex for s in size for c in color
#         if not (g == 'F' and s == 'X')]
# print(tags)

