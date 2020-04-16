import sys

N = int(sys.stdin.readline())
order = list()

for i in range(N):
    order.append(int(sys.stdin.readline()))

order.sort()

for _ in order:
    sys.stdout.write(str(_) + '\n')