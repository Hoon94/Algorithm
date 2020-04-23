import sys

N = int(sys.stdin.readline())
arr = []
count = 0

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
arr_one = list(set(arr))

print("%.f"%(sum(arr)/N))

print(arr[N//2])

for i in range(len(arr_one)):
    if count < arr.count(arr_one[i]):
        count = arr.count(arr_one[i])
        result = arr_one[i]

print(result)

print(arr[-1] - arr[0])