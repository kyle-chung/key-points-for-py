*args和**kwargs主要用于函数定义。你可以将不定数量的参数传递给一个函数。这里的不定指的是预先并不知道函数使用者会传递多少个参数给你

*args是用来发送一个非键值对的可变数量的参数列表给一个函数
下面这段代码演示了如何使用args

def test_args(first, *args):
    print('Required argument: ', first)
    print(type(args))
    for v in args:
        print ('Optional argument: ', v)

test_args(1, 2, 3, 4)

第一个参数是必须要传入的参数，所以使用了第一个形参，而后面三个参数则作为可变参数列表传入了实参，并且是作为元组tuple来使用的
代码的运行结果如下

Required argument:  1
<class 'tuple'>
Optional argument:  2
Optional argument:  3
Optional argument:  4


**kwargs允许你将不定长度的键值对，作为参数传递给一个函数
下面这段代码演示了如何使用kwargs

def test_kwargs(first, *args, **kwargs):
   print('Required argument: ', first)
   print(type(kwargs))
   for v in args:
      print ('Optional argument (args): ', v)
   for k, v in kwargs.items():
      print ('Optional argument %s (kwargs): %s' % (k, v))

test_kwargs(1, 2, 3, 4, k1=5, k2=6)

正如前面所说的，args类型是一个tuple，而kwargs则是一个字典dict，并且args只能位于kwargs的前面
代码的运行结果如下

Required argument:  1
<class 'dict'>
Optional argument (args):  2
Optional argument (args):  3
Optional argument (args):  4
Optional argument k2 (kwargs): 6
Optional argument k1 (kwargs): 5


标准参数与*args、**kwargs在使用时的顺序
some_ func(fargs, *args, **kwargs)
