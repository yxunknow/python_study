#
# sign_up.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/11/18 19:12
# 

username = input('input username:')
password = input('input password:')

with open('d:/python/user', mode='w', encoding='utf-8') as user:
    user.write(username + ' ' + password)
    print('sign up success with:', username, password)
