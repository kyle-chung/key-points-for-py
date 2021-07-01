a = [1,2,3,4]

# can stop
for pos,i in enumerate(a[::-1]):
    a.append(1)
    
# can stop
for i in a[::-1]:
    a.append(1)
    
# can not stop
for i in a:
    a.append(1)
