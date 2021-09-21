简单使用
f-string用大括号 {} 表示被替换字段，其中直接填入替换内容：

>>> name = 'Eric'
>>> f'Hello, my name is {name}'
'Hello, my name is Eric'
 
>>> number = 7
>>> f'My lucky number is {number}'
'My lucky number is 7'

表达式求值与函数调用
f-string的大括号 {} 可以填入表达式或调用函数，Python会求出其结果并填入返回的字符串内：

>>> f'A total number of {24 * 8 + 4}'
'A total number of 196'

>>> name = 'ERIC'
>>> f'My name is {name.lower()}'
'My name is eric'

引号、大括号与反斜杠
f-string大括号内所用的引号不能和大括号外的引号定界符冲突，可根据情况灵活切换 ' 和 "：
若 ' 和 " 不足以满足要求，还可以使用 ''' 和 """：

>>> f'I am {"Eric"}'
'I am Eric'
>>> f'I am {'Eric'}'
  File "<stdin>", line 1
    f'I am {'Eric'}'
                ^
SyntaxError: invalid syntax

lambda表达式
f-string大括号内也可填入lambda表达式，但lambda表达式的 : 会被f-string误认为是表达式与格式描述符之间的分隔符
为避免歧义，需要将lambda表达式置于括号 () 内：

>>> f'result is {lambda x: x ** 2 + 1 (2)}'
  File "<fstring>", line 1
    (lambda x)
             ^
SyntaxError: unexpected EOF while parsing
 
>>> f'result is {(lambda x: x ** 2 + 1) (2)}'
'result is 5'
