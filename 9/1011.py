import math

a = int(input())

for i in range(a):
    x, y = map(int, input().split())

    distance = y - x

    b = int(math.sqrt(distance))
    c = b + 1

    if  b == 1:
        print(distance)
    elif distance > b * c + 1:
        print(b + c)
    elif distance >= b ** 2 + 1:
        print(b * 2)
    else:
        print(b * 2 - 1)