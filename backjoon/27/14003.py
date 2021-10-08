from bisect import bisect_left

N = int(input())
arr = [0] + list(map(int, input().split()))
d = [0] * (N + 1)
cmp = [-1000000001]
maxVal = 0

for i in range(1, N + 1):
    if cmp[-1] < arr[i]:
        cmp.append(arr[i])
        d[i] = len(cmp) - 1
        maxVal = d[i]
    else:
        d[i] = bisect_left(cmp, arr[i])
        cmp[d[i]] = arr[i]
print(maxVal)

res = []
for i in range(N, 0, -1):
    if d[i] == maxVal:
        res.append(arr[i])
        maxVal -= 1
res.reverse()
print(*res)
