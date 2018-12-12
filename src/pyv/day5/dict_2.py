#
# dict_2.py.py
# Created in Intelij IDEA
# 
# dict nested and exercise
# 
# @author Mevur
# @date 12/04/18 20:13
# 

# nested dict
msg = {
    'user': {
        'name': 'java',
        'token': 'adiahoiafwbiada'
    },
    'code': 200,
    'info': 'ok'
}

print(msg.get('user', 'no user key'))
