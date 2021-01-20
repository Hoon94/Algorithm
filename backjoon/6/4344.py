import sys

c = int(input())

for i in range(c):
    a = list(map(int, sys.stdin.readline().split()))
    b = a[1:]
    over = 0.0
    for j in range(len(b)):

        if b[j] > (sum(b)/a[0]):
            over = over + 1

    print('{:0.3f}'.format(round(over/a[0]*100, 3)) + '%')