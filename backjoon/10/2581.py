m = int(input())
n = int(input())
num = []

for i in range(m, n+1):
    j = 2
    while i//j > 0:
        if i == j:
            num.append(i)
        elif i%j == 0:
            break
        j += 1


if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(min(num))