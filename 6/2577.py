import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

value = a*b*c

string = list(map(int, str(value)))

for i in range(10):
    print(string.count(i))