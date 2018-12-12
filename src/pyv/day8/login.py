#
# login.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/11/18 19:17
# 

user = open('d:/python/user', mode='r', encoding='utf-8')
users = user.readlines()
t = 0
while t < 3:
    username = input('input username:')
    password = input('input password:')
    info = username + ' ' + password
    result = False
    for v in users:
        if v == info:
            result = True
            break
    if result:
        print('login success')
        break
    else:
        print('error')
        t = t + 1
