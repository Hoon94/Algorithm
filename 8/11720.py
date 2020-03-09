import sys

a = int(sys.stdin.readline())

b = int(sys.stdin.readline())
b_list = list(map(int, str(b)))
print(sum(b_list))