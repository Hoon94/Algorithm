n = int(input())
coins = list(map(int, input().split()))
answer = 1
coins.sort()

for coin in coins:
    if coin > answer:
        break
    answer += coin

print(answer)
