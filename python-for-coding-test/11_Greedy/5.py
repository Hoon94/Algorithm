n, m = map(int, input().split())
weight = list(map(int, input().split()))
answer = []

for i in range(n - 1):
    for j in range(i, n):
        if weight[i] != weight[j]:
            answer.append((i + 1, j + 1))

print(len(answer))
