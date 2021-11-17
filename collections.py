这个模块实现了特定目标的容器，以提供Python标准内建容器 dict、list、set、tuple 的替代选择

Counter：字典的子类，提供了可哈希对象的计数功能
defaultdict：字典的子类，提供了一个工厂函数，为字典查询提供了默认值
OrderedDict：字典的子类，保留了他们被添加的顺序
namedtuple：创建命名元组子类的工厂函数
deque：类似列表容器，实现了在两端快速添加(append)和弹出(pop)
ChainMap：类似字典的容器类，将多个映射集合到一个视图里面


Counter
Counter是一个dict子类，主要是用来对你访问的对象的频率进行计数

# 统计字符出现的次数
>>> import collections
>>> collections.Counter('hello world')
Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# 统计单词数
>>> collections.Counter('hello world hello world hello nihao'.split())
Counter({'hello': 3, 'world': 2, 'nihao': 1})



defaultdict
collections.defaultdict(default_factory)为字典的没有的key提供一个默认的值
参数应该是一个函数，当没有参数调用时返回默认值。如果没有传递任何内容，则默认为None

>>> d = collections.defaultdict()
>>> d
defaultdict(None, {})

defaultdict的一个典型用法是使用其中一种内置类型(如str、int、list或dict)作为默认工厂，因为这些内置类型在没有参数调用时返回空类型。

使用str作为default_factory的例子：

>>> d = collections.defaultdict(str)
>>> d
defaultdict(<class 'str'>, {})
>>> d['hello']
''
>>> d
defaultdict(<class 'str'>, {'hello': ''})
# 普通字典调用不存在的键时，将会抛异常
>>> e = {}
>>> e['hello']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'hello'
  
使用int作为default_factory的例子：

>>> from collections import defaultdict
>>> fruit = defaultdict(int)
>>> fruit['apple'] += 2 
>>> fruit
defaultdict(<class 'int'>, {'apple': 2})
>>> fruit
defaultdict(<class 'int'>, {'apple': 2})
>>> fruit['banana']  # 没有对象时，返回0
0
>>> fruit
defaultdict(<class 'int'>, {'apple': 2, 'banana': 0})

使用list作为default_factory的例子：

>>> s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')]
>>> d = collections.defaultdict(list)
>>> for k,v in s:
...      d[k].append(v)
... 
>>> d
defaultdict(<class 'list'>, {'NC': ['Raleigh', 'Asheville'], 'VA': ['Richmond'], 'WA': ['Seattle']})



OrderedDict
Python字典中的键的顺序是任意的:它们不受添加的顺序的控制
collections.OrderedDict类提供了保留他们添加顺序的字典对象

>>> from collections import OrderedDict
>>> o = OrderedDict()
>>> o['key1'] = 'value1'
>>> o['key2'] = 'value2'
>>> o['key3'] = 'value3'
>>> o
OrderedDict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

如果在已经存在的key上添加新的值，将会保留原来的key的位置，然后覆盖value值

>>> o['key1'] = 'value5'
>>> o
OrderedDict([('key1', 'value5'), ('key2', 'value2'), ('key3', 'value3')])



namedtuple
三种定义命名元组的方法：第一个参数是命名元组的构造器（如下的：Person，Human）

>>> from collections import namedtuple
>>> Person = namedtuple('Person', ['age', 'height', 'name'])
>>> Human = namedtuple('Human', 'age, height, name')
>>> Human2 = namedtuple('Human2', 'age height name')

实例化命令元组

>>> tom = Person(30,178,'Tom')
>>> jack = Human(20,179,'Jack')
>>> tom
Person(age=30, height=178, name='Tom')
>>> jack
Human(age=20, height=179, name='Jack')
>>> tom.age #直接通过  实例名+.+属性 来调用
30
>>> jack.name
'Jack'



ChainMap
一个 ChainMap 将多个字典或者其他映射组合在一起，创建一个单独的可更新的视图。 如果没有 maps 被指定，就提供一个默认的空字典 
ChainMap是管理嵌套上下文和覆盖的有用工具。

>>> from collections import ChainMap
>>> d1 = {'apple':1,'banana':2}
>>> d2 = {'orange':2,'apple':3,'pike':1}
>>> combined_d = ChainMap(d1,d2)
>>> reverse_combind_d = ChainMap(d2,d1)
>>> combined_d 
ChainMap({'apple': 1, 'banana': 2}, {'orange': 2, 'apple': 3, 'pike': 1})
>>> reverse_combind_d
ChainMap({'orange': 2, 'apple': 3, 'pike': 1}, {'apple': 1, 'banana': 2})
>>> for k,v in combined_d.items():
...      print(k,v)
... 
pike 1
apple 1
banana 2
orange 2
>>> for k,v in reverse_combind_d.items():
...      print(k,v)
... 
pike 1
apple 3
banana 2
orange 2




