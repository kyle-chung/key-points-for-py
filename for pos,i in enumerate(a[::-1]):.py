a = [1,2,3,4]

# can stop
for pos,i in enumerate(a[::-1]):
    a.append(1)
    
# can stop
for i in a[::-1]:
    a.append(1)

切片是引用新的对象，此时在循环中res[:]是不更新的

# can stop
for pos,i in enumerate(a):
    a.append(1)

# can not stop
for i in a:
    a.append(1)
