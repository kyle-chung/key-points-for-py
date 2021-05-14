a, b = b , a + b

a = 1
b = 2
c = a, a+b  # 这里 c=(1,3)
print type(c)  # <type 'tuple'>
a, b = c
print a, b  # 1 3

赋值运算，先计算赋值号（也就是=号左边的，再赋值）
