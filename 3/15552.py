import sys
a = int(input())

'''
for i in range(a):
    b, c = map(int, input().split())
    print(b + c)
'''

for line in range(a):
    b, c = map(int, sys.stdin.readline().split())
    print(b+c)