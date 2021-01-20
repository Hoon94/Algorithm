b = []
x = []
y = []

for i in range(3):
    a = list(map(int, input().split()))
    b.append(a)

for j in range(3):
    x.append(b[j][0])
    y.append(b[j][1])

for k in range(3):
    if x.count(x[k]) == 1:
        c = x[k]
    if y.count(y[k]) == 1:
        d = y[k]

print(c, d)