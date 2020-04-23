N = int(input())
point = []

for i in range(N):
    point.append(list(map(int, input().split())))

point.sort()

for i, j in point:
    print(i, j)