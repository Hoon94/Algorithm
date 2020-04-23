import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
case = []

for i in range(K):
    x, y = sys.stdin.readline().split()
    case.append((int(x), int(y)))

case = list(set(case))
case.sort(key= lambda x : (-x[0], -x[1]))
print(case)

for i in range(len(case)):

    if case[i][0] > case[i][1]:
        case1 = num[0:case[i][0]]
        case1.sort()
        num[0:case[i][0]] = case1

    case2 = num[0:case[i][1]]
    case2.sort(reverse=True)
    num[0:case[i][1]] = case2

for i in num:
    print(i, end= ' ')