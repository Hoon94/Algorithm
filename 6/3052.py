import sys

b = []
num = 0

for i in range(10):
    a = int(sys.stdin.readline())
    b.append(a%42)

for i in range(42):
    if i in b:
        num = num + 1

print(num)