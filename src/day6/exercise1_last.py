#
# exercise1_last.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/05/18 18:35
# 

nums = {
    "min": [],
    "max": []
}

li = (22, 11, 23, 151, 41, 52, 88, 1, 209, 314, 19)
for i in li:
    if i >= 66:
        nums['max'].append(i)
    else:
        nums['min'].append(i)

print(nums)
