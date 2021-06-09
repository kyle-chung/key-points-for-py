TypeError: ‘NoneType’ object is not callable

分析解决：
callable(可调用)对象是指一个后面可以加 ‘()’的对象
既然报错是 ‘不可调用’，那就去掉调用函数的 ‘()’ 即可。
