# stage knowledge conclusion 

## grammar comparision
### python2
print('value') print 'value'  
range() xrange()  
raw_input()
### python3
print('value')  
range()  
input() 

## == vs is
1. =  
assign symbol.  
in generally, this symbol is assigning a memory address to a variable
2. ==  
compare with value
3. is  
compare with memory address

## id
id(object): get memory address of an object

## number, string and other
### number
```$xslt
num1 = 6
num2 = 6
# in a small data pool
# number belong to small data poll in range of -5 to 256
# allocate a same memory address,
# ohterwise allocate different memory address
```
### string
```$xslt
# small data pool of string
# 1. no special characters
# 2. s*20(s is a single letter) is in small data, s*21 is not in
```

### the other
except number or string type, other object has no small data pool

## code in py3 and py3
1. ascii  
一个字符用8位表示，一个字节  
2. unicode    
一个字符用32位表示，四个字节  
3. utf-8
一个字符用8位表示，一个字节  
一个中文汉字用3个字节表示  
4. gbk  
一个字符用8位，1个字节表示  
一个汉字用2个字节表示  


各个编码之间的二进制无法相互识别，会产生乱码。  
unicode不适合于文件存储和传输，文件存储传输多用GBK， utf8， ascii  

### py3
string in py3 is storaged with unicode code in memory.  

### bytes in py3
declaration a bytes data
b = b'content'
