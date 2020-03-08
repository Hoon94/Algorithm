import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
c = max(b)

for i in range(len(b)):
    b[i] = b[i]/c*100

print(sum(b)/len(b))