#
# exercise2_last.py
# Created in Intelij IDEA
# 
# good car cli program
# 
# @author Mevur
# @date 12/05/18 18:39
#
goods = ('手机', '电脑', '平板', '笔记本', 'mp3', 'iPod')

'''
print good in list
'''

# use flag to improve the ability of maintains
flag = True
while flag:
    # print goods
    for good in goods:
        print('{}\t\t{}'.format(goods.index(good) + 1, good))
    # accept user input
    which = input('输入商品序号(q/Q退出):')
    # check exit
    if which.upper() == 'Q':
        print('谢谢使用')
        break
    # validate input
    if which.isdigit():
        which = int(which)
        # validate range
        if which > len(goods) or which < 0:
            print('商品不存在')
        else:
            print(goods[which - 1])
            pass
    else:
        print('请输入数字序号')
