N, M = map(int, input().split())
n = list(map(int, input().split()))
case = 0

n.sort()

for i in range(N - 1):
    case += i