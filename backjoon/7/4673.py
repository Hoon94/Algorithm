def self_func(a: int):
    c = str(a)
    value = a
    for i in range(len(c)):
        value = int(c[i]) + value
    
    if value in b and value != a:
        b.remove(value)

b = []

for i in range(10000):
    b.append(i+1)

for i in range(10000):
    self_func(i+1)

for i in range(len(b)):
    print(b[i])