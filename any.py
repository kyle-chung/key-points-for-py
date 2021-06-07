any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。

元素除了是 0、空、FALSE 外都算 TRUE。

函数等价于：

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
