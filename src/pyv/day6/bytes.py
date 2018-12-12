#
# bytes.py
# Created in Intelij IDEA
# 
# convert str to bytes
# 
# @author Mevur
# @date 12/05/18 19:54
# 

str = 'taiwan province, china'
sutf8 = str.encode('utf-8')
print(sutf8)

strChinese = '中国台湾省'
s2 = strChinese.encode('utf-8')
print(s2)

s3 = strChinese.encode('gbk')
print(s3)

s4 = b'23cha'
print(s4)
