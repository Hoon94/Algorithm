a = [ 1, 3, 5, 7, 9]
b = [ 13, 17]
c = a + b
print(c)
b[0] = -1
print(b)
d = [ e + 1 for e in a ]
print(d)
d.append(b[0]+1)
d.append(b[-1] + 1)
print(d)
print(d[:-2])
