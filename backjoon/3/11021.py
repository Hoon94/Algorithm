import sys

a = int(input())

for i in range(a):
    b,c = map(int, sys.stdin.readline().split())
    print("Case #{}:".format(i+1), b+c)