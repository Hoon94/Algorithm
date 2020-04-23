N = int(input())
point = []

for i in range(N):
    point.append(list(map(int, input().split())))

point.sort(key=lambda x: (x[0], x[1]))
# x는 x[0] 다음 x[1]이 된다.

for i, j in point:
    print(i, j)