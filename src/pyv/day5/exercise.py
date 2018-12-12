#
# exercise.py.py
# Created in Intelij IDEA
# 
# day exercise
# input a string
# replace all letter with blank
# and find number in string
# 
# @author Mevur
# @date 12/04/18 20:28
# 

info = input('>>>input info:\n')
for i in info:
    if i.isalpha():
        info = info.replace(i, ' ')
nums = info.split()
for n in nums:
    print(n)
