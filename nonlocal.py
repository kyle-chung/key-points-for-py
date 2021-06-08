nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。

def work():
    x = 0
    def new_work():
        nonlocal x
        x=x+3
        return x
    return new_work
         
f=work()
print(f())
print(f())
print(f())

打印结果:3,6,9


使用global 实现

a =0
def new_work():
    global a
    a=a+3
    return a
print(new_work())
print(new_work())
print(new_work())

打印结果:3,6,9
