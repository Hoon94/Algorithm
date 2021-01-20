a = list(map(int, input().split()))

x = min(a[2] - a[0], a[0])
y = min(a[3] - a[1], a[1])

if x > y:
    print(y)
else:
    print(x)