T = int(input())

for i in range(T):
    a = list(map(int, input().split()))
    distance = ((a[0]-a[3])**2 + (a[1]-a[4])**2)**0.5
    rmax = a[2] + a[5]
    rmin = abs(a[2] - a[5])

    if distance == 0:
        if a[2] == a[5]:
            print(-1)
        else:
            print(0)
    else:
        if distance == rmax or distance == rmin:
            print(1)
        elif rmin < distance < rmax:
            print(2)
        else:
            print(0)