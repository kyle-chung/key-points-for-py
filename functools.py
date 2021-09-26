reduce

在 Python2 中等同于内建函数 reduce
函数的作用是将一个序列归纳为一个输出
reduce(function, sequence, startValue)

from functools import reduce

l = range(1,50)
print(reduce(lambda x,y:x+y, l))
# 1225
