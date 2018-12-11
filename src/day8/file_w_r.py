#
# file_w_r.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/11/18 18:27
# 

f = open('d:/python/log', mode='r+', encoding='utf-8')
# read file and move cursor to eof
# c = f.read()
# print(c)
# # f.write('write over\n')
# # f.close()
#
# # feature
# print("============")
# f.seek(0)
# # read method return character
# pc = f.read(10)
# print(pc)

# =======华丽の分割线
# read by character
# seek by byte
# =================

# set cursor
# seek move cursor by byte
# use 3 bytes to present a chinese character in utf-8 coding
# f.seek(13)
# c = f.read()
# print(c)


# find current cursor
# tmp = f.read(12)
# # return location of file cursor
# cc = f.tell()
# print(cc)

# f.readable()  check the file weather readable or not
# readLine() read file line by line
# writable check the file weather writable or not

f.seek(0)
# line = f.readline()
# print(line)
# for l in f:
#   print(l)


# readLines: return a list contains all lines of file
# li = f.readlines()
# print(li)

# wtf!
# tru = f.read()
# print(tru)
# f.write('2133221waew')
# f.seek(0)
# print(f.read())


# with
# use resources and auto close the resources
# open multi-resource at same time
with open('d:/python/log', mode='r+', encoding='utf-8') as fi:
    content = fi.read()
    print(content)

