n = int(input())
data = list(map(int, input().split()))

data.sort()
print(data[n // 2 - 1])
