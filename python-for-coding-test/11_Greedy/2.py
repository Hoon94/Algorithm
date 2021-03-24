s = list(map(int, input().replace('0', '')))
answer = 1

for i in s:
    answer *= i

print(answer)
