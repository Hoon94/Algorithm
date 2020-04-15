N, M = map(int, input().split())
card = list(map(int,input().split(' ')))

card.sort()
result = 0

for i in range(N - 1, 1, -1):
    for j in range(i - 1, 0, -1):
        for k in range(j - 1, -1, -1):
            if card[i] + card[j] + card[k] <= M and result < card[i] + card[j] + card[k]:
                result = card[i] + card[j] + card[k]
                break

print(result)