import sys

t = int(sys.stdin.readline())
for case in range(t):
    n = int(sys.stdin.readline())
    parents = [0 for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        parents[b] = a

    a, b = map(int, sys.stdin.readline().split())
    a_parents = [a]
    b_parents = [b]

    while parents[a]:
        a_parents.append(parents[a])
        a = parents[a]

    while parents[b]:
        b_parents.append(parents[b])
        b = parents[b]

    a_spot = len(a_parents) - 1
    b_spot = len(b_parents) - 1
    while a_parents[a_spot] == b_parents[b_spot]:
        a_spot -= 1
        b_spot -= 1

    print(a_parents[a_spot + 1])
