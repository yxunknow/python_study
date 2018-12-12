
def max(a, b):
    return a if a > b else b

def max3(a, b, c):
    return max(max(a, b), c)


# print(max3(1, 3, 9))

# nested def
def outer():
    a = 1
    def inner():
        # a is read-only here
        # nonlocal 声明上层局部变量， 只作用在局部域
        # nonlocal a  # a is writable now
        print('inner')
    inner()
    print('outer')

outer()


# nonlocal: 只能用于局部变量，找到离当前位置最近一层的一个局部变量
# global: 作用在全局变量上，从全局范围寻找一个变量

# function is also a type
# 第一类对象
# 在运行时创建
# 可以作为函数的参数和返回值
# 可以传入变量的实体


