#
# file_mode.py
# Created in Intelij IDEA
# 
# Write Some Describe of this class here
# 
# @author Mevur
# @date 12/07/18 23:23
# 

f = open('d:/python/log', mode='r+', encoding='utf-8')
# in this mode, when file opened, the cursor is at begin of file
log = f.read()
print(log)
f.write('ok, i am readsqeqe2a\n')
# read doesn't work here
newLog = f.read(0)
print(newLog)
f.close()

# when operate with binary mode, the encoding param can be omited

# read and write
# r+ or r+b

# write and read
# w+
