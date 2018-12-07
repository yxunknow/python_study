#
# file_operate.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/07/18 22:30
# 

# 1. file path
# absolute filepath
# d:/xx/xx/x.txt
# relative filepath
# ../xx/x/x.txt

# 2. file encode

# 3. file permission

# ===================
# =====read file=====
# ===================
# absolute filepath

'''
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
'''
# f = open('d:/python/test.py', mode='r', encoding='utf-8')
# fileContent = f.read()
# print(fileContent)
# used file and release it when you don't need it more
# f.close()

# relative filepath
# fi = open('../day7/datatype.py', mode='r', encoding='utf-8')
# convert bytes to str in read function
# content = fi.read()
# print(content)
# fi.close()

# read with binary
# fb = open('d:/python/test.py', mode='rb')
# return a bytes data
# fbc = fb.read()
# print(fbc)
# print(type(fbc))
# fb.close()

# write file
# delete old file content and write new content
# override mode
# log = open('d:/python/log', mode='w', encoding='utf-8')
# log.write('hello world from python')
# log.close()

# write binary
# logb = open('d:/python/logb', mode='wb')
# logb.write('中国23'.encode('utf-8'))
# logb.close()

# append
# flog = open('d:/python/log', mode='a', encoding='utf-8')
# flog.write('wwsd\n')
# flog.write('wwsdwa\n')
# flog.write('wwsdadawa\n')
# flog.close()

# append binary
flogb = open('d:/python/log', mode='ab')
flogb.write('\nwdadawdadwa2\n'.encode('utf-8'))
flogb.close()
