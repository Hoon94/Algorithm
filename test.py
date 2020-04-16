a = [1,2,3,4,5,6,7,8,9] 
b = a 
c = list(a) 
d = a.copy() 
#b[0] = 10
c[0] = 9
d[0] = 8
''' 
from copy import deepcopy 
e = [[1,2],[3,4],[5,6]] 
f = e.copy() 
g = deepcopy(e) 
e[0] = [9,8]
''' 
print(a) 
print(b)
print(c)
print(d)
'''
print(e)
print(g)
print(f)
'''