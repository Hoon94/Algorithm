import sys

a, b = map(int, sys.stdin.readline().split())
x = sys.stdin.readline().split()

for i in range(a):
    if(int(x[i]) < b):
        print(x[i], end=' ')
