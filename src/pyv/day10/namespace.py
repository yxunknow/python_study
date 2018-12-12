# 内置命名空间 only one
# python解释器启动时就加载到内存
# 内置名称在python解释器加载时就被放入内存中，如print， input
# 全局命名空间 only one
# 程序顺序执行的过程加载到内存中
# 存放我们定义的全局变量和函数
# 局部命名空间 multiple independent
# 函数内部定义的变量，在函数执行时被放入内存

# 在局部可以使用全局命名空间和内置命名空间
# 在全局可以使用内置命名空间, 不能使用局部空间
# 在内置命名空间中无法使用局部和全局命名空间

# 依赖倒置原则： 程序顶层可以依赖底层，而底层不能依赖顶层

# when define a same identifier with inset namespace in global namespace,
# when use that identifier, the definition in global will be used
# def input():
#     print('def an input method')
#
# # this call will execute above custom def function
# input()

# 当在当前空间存在某个标示符时，不会向上一级命名空间查找。

# def func():  # func is a reference of memory address
#    ...
# func()  # call function

# scope

# global scope
#
# local scope

# use global keyword to define a global identifier at partial scope
# def func():
#    global a
#    a = 2
# when func is executed, a = 2 will be usable in anywhere

# locals() return all local variables at its current scope
# globals() return all global variables, includes build-in variables

