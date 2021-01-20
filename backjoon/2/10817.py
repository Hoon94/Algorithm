a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a > b:
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        print(b)
