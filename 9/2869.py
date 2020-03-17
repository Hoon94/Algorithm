a = list(map(int, input().split()))

day = a[0] - a[1]
value = (a[2] - a[1])//day

if (a[2] - a[1]) % day == 0:
    print(value)
else:
    print(value + 1)