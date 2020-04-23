import sys
from collections import deque

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
case = deque()

for i in range(K):
    x, y = sys.stdin.readline().split()
    while len(case) != 0 and abs(case[-1]) <= int(x):
        case.pop()
    case.append(int(x))
    while len(case) != 0 and abs(case[-1]) <= int(y):
        case.pop()
    case.append(-int(y))

print(case)


for i in range(len(case)):

    if case[i] >= 0:
        case1 = num[0:case[i]]
        print(case1)
        case1.sort()
        num[0:case[i]] = case1
    else:
        case2 = num[0:abs(case[i])]
        case2.sort(reverse=True)
        num[0:abs(case[i])] = case2

for i in num:
    sys.stdout.write(str(i)+' ')

'''
Test example

10
4 1 5 2 3 10 8 11 15 6
6
3 2
4 5
5 4
3 2
2 1
3 1

'''