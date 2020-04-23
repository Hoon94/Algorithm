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

ascendidx = max(max(case), abs(min(case))) - 1
descendidx = 0
sortnumidx = ascendidx

num[:ascendidx + 1] = sorted(num[:ascendidx + 1])
sortnum = num.copy()

case.append(0)
curr = case.popleft()

while len(case) > 0:
    after = case.popleft()

    diff = abs(abs(curr) - abs(after))
    if curr > 0:
        for i in range(diff):
            sortnum[sortnumidx] = num[ascendidx]
            ascendidx -= 1
            sortnumidx -= 1
    else:
        for i in range(diff):
            sortnum[sortnumidx] = num[descendidx]
            descendidx += 1
            sortnumidx -= 1
    
    curr = after

for i in sortnum:
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