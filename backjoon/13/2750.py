N = int(input())
order = list()

for i in range(N):
    order.append(int(input()))

order.sort()

for _ in order:
    print(_)